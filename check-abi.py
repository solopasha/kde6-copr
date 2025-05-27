#!/usr/bin/python3 -u

# Copyright (c) 2018 - Mathieu Bridon <bochecha@daitauha.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import argparse
import filecmp
import json
import os
import re
import subprocess
import sys
import tarfile
from fnmatch import fnmatch

from elftools.elf.elffile import ELFFile

ABRT_EXIT_CODE = -6
SEGV_EXIT_CODE = -11


class AbiCheckResult:
    def __init__(self, abi_was_broken, details, core_dumped, command):
        self.abi_was_broken = abi_was_broken
        self.details = details
        self.core_dumped = core_dumped
        self.command = command


def get_parser():
    parser = argparse.ArgumentParser(
        description="Compare the ABI of two revisions",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("--old", required=True, help="old sysroot")
    parser.add_argument("--new", required=True, help="new sysroot")

    parser.add_argument(
        "--suppressions", metavar="PATH", help="specify a suppression file"
    )

    parser.add_argument(
        "--abidiff-suppressions",
        metavar="PATH",
        help="specify a suppression file for abidiff",
    )

    parser.add_argument("--forward-compatible", action="store_true")

    parser.add_argument(
        "--archive-on-core",
        action="store_true",
        help="create a tarball of the binaries that cause abidiff to core dump",
    )
    parser.add_argument(
        "--archive-directory-parent",
        default=os.path.abspath(os.curdir),
        help="parent directory in which the archive directory is created",
    )
    parser.add_argument(
        "--full-abi-diff", type=int, default=False, help="Force full ABI diff on"
    )

    return parser


def format_title(title, level):
    box = {
        1: {"tl": "╔", "tr": "╗", "bl": "╚", "br": "╝", "h": "═", "v": "║"},
        2: {"tl": "┌", "tr": "┐", "bl": "└", "br": "┘", "h": "─", "v": "│"},
    }[level]
    hline = box["h"] * (len(title) + 2)

    return "\n".join(
        [
            f"{box['tl']}{hline}{box['tr']}",
            f"{box['v']} {title} {box['v']}",
            f"{box['bl']}{hline}{box['br']}",
        ]
    )


def check_command(cmd):
    try:
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        sys.exit(f"Please install the {cmd[0]} command")


def sanity_check():
    check_command(["abidiff", "--version"])
    check_command(["file", "--version"])
    check_command(["objdump", "--version"])


def sanitize_path(name):
    return name.replace("/", "-")


def get_mimetype(path):
    return subprocess.check_output(
        ["file", "--mime-type", "--brief", path], encoding="utf-8"
    ).strip()


def get_soname(path):
    out = subprocess.check_output(
        ["objdump", "-x", path], encoding="utf-8", stderr=subprocess.STDOUT
    ).strip()

    for line in out.split("\n"):
        if "SONAME" in line:
            return line.split()[-1]

    return None


def get_library_key(path):
    soname = get_soname(path)

    if soname is None:
        return os.path.basename(path)

    return f"{soname}"


def get_libraries(tree):
    seen = set()
    libs = {}

    libdir = os.path.join(tree, "usr", "lib64")

    for dirpath, _, filenames in os.walk(libdir):
        for filename in sorted(filenames):
            if not fnmatch(filename, "lib*.so*") or fnmatch(filename, "*.debug"):
                continue

            library = os.path.join(dirpath, filename)
            realpath = os.path.relpath(os.path.realpath(library))

            if realpath in seen:
                # There were symlinks, no need to compare more than once
                continue

            seen.add(realpath)

            if get_mimetype(realpath).startswith("text/"):
                # This is probably a GNU ld script, but not a C library anyway
                continue

            lib_key = get_library_key(realpath)
            rel_path = os.path.relpath(realpath, start=tree)

            if lib_key in libs:
                if not filecmp.cmp(os.path.join(tree, libs[lib_key]), realpath):
                    raise RuntimeError(
                        f"{libs[lib_key]} and {rel_path} libraries have the same SONAME but not the same content."
                    )

            else:
                libs[lib_key] = rel_path

    return libs


def file_sha256(filename):
    try:
        checksum = os.getxattr(filename, "user.checksum.sha256")
    except OSError:
        return None

    return checksum


def fast_file_check(first, second):
    first_sha256 = file_sha256(first)
    second_sha256 = file_sha256(second)
    if first_sha256 is None or second_sha256 is None:
        return False
    return first_sha256 == second_sha256


def compare_abi(
    old_library,
    old_debug_dir,
    old_include_dir,
    new_library,
    new_debug_dir,
    new_include_dir,
    forward_compatible,
):
    options = ["--drop-private-types"]
    if not forward_compatible:
        # This is confusing. abidiff complains of added symbols only
        # if this option is not passed.
        options.append("--no-added-syms")
    cmd = [
        "abidiff",
        "--headers-dir1",
        old_include_dir,
        "--headers-dir2",
        new_include_dir,
        "--debug-info-dir1",
        old_debug_dir,
        "--debug-info-dir2",
        new_debug_dir,
        old_library,
        new_library,
    ] + options
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8"
    )
    out = result.stdout.strip()
    core_dumped = result.returncode in (ABRT_EXIT_CODE, SEGV_EXIT_CODE)

    return AbiCheckResult(bool(result.returncode), out, core_dumped, cmd)


def get_debugaltlink(debug_file):
    dirname = os.path.dirname(debug_file)
    with ELFFile.load_from_path(debug_file) as elffile:
        altlink = elffile.get_section_by_name(".gnu_debugaltlink")
        if altlink is None:
            return None
        return os.path.join(dirname, altlink.data().split(b"\x00")[0].decode("latin-1"))


def create_binary_archive(
    archive_directory,
    old_debug_dir,
    old_library,
    old_checkout,
    new_debug_dir,
    new_library,
    new_checkout,
):
    old_debug_file = (
        os.path.join(old_debug_dir, os.path.relpath(old_library, old_checkout))
        + ".debug"
    )
    new_debug_file = (
        os.path.join(new_debug_dir, os.path.relpath(new_library, new_checkout))
        + ".debug"
    )
    altlink = get_debugaltlink(old_debug_file)
    files = [old_library, old_debug_file, new_library, new_debug_file]
    if altlink is not None:
        prefix = os.path.commonpath((altlink, old_checkout))
        rel_path = os.path.relpath(altlink, prefix)
        files.extend(
            (os.path.join(old_checkout, rel_path), os.path.join(new_checkout, rel_path))
        )
    tar_file = os.path.join(
        archive_directory, f"{os.path.basename(old_library)}.tar.xz"
    )
    with tarfile.open(tar_file, "w:xz") as tar:
        for file in files:
            tar.add(file)


def create_header_archive(archive_directory, old_include_dir, new_include_dir):
    header_tar = os.path.join(archive_directory, "headers.tar.xz")
    if os.path.exists(header_tar):
        return

    with tarfile.open(header_tar, "w:xz") as tar:
        tar.add(old_include_dir)
        tar.add(new_include_dir)


def compare_tree_abis(
    old_checkout,
    new_checkout,
    suppression_file_path,
    forward_compatible,
    archive_on_core,
    archive_directory,
    full_abi_diff,
):
    print(format_title("Comparing ABIs", level=1), end="\n\n")
    success = True

    old_libs = get_libraries(old_checkout)
    new_libs = get_libraries(new_checkout)

    all_keys = set(new_libs.keys()) | set(old_libs.keys())

    with open(suppression_file_path, "r", encoding="utf-8") as filehandle:
        suppression_rules = json.load(filehandle)
    suppression_regex = "|".join(suppression_rules)
    suppression_regex_obj = re.compile(suppression_regex)

    for lib_key in all_keys:
        if suppression_regex_obj.match(lib_key):
            print(f"Skipping file {lib_key}", file=sys.stderr)
            continue

        try:
            old_relpath = old_libs[lib_key]

        except KeyError:
            if forward_compatible:
                title = format_title(f"ABI Break: {lib_key}", level=2)
                print(
                    f"{title}\n\nLibrary was added in {new_checkout}\n", file=sys.stderr
                )
                success = False
            continue

        try:
            new_relpath = new_libs[lib_key]

        except KeyError:
            title = format_title(f"ABI Break: {lib_key}", level=2)
            print(
                f"{title}\n\nLibrary does not exist any more in {new_checkout}\n",
                file=sys.stderr,
            )
            success = False
            continue

        old_library = os.path.join(old_checkout, old_relpath)
        old_debug_dir = os.path.join(old_checkout, "usr", "lib", "debug")
        old_include_dir = os.path.join(old_checkout, "usr", "include")

        new_library = os.path.join(new_checkout, new_relpath)
        new_debug_dir = os.path.join(new_checkout, "usr", "lib", "debug")
        new_include_dir = os.path.join(new_checkout, "usr", "include")

        if not full_abi_diff and fast_file_check(old_library, new_library):
            continue

        if not full_abi_diff and filecmp.cmp(old_library, new_library, shallow=False):
            # Full file equality, ABI cannot have changed
            continue

        result = compare_abi(
            old_library,
            old_debug_dir,
            old_include_dir,
            new_library,
            new_debug_dir,
            new_include_dir,
            forward_compatible,
        )

        if result.abi_was_broken:
            title = format_title(f"ABI Break: {lib_key}", level=2)
            print(f"{title}\n\n{result.details}\n", file=sys.stderr)
            success = False

            if result.core_dumped and archive_on_core:
                print(
                    f"abidiff core dumped, command was:\n{' '.join(result.command)}",
                    file=sys.stderr,
                )
                create_binary_archive(
                    archive_directory,
                    old_debug_dir,
                    old_library,
                    old_checkout,
                    new_debug_dir,
                    new_library,
                    new_checkout,
                )
                create_header_archive(
                    archive_directory, old_include_dir, new_include_dir
                )

        elif result.details:
            title = format_title(f"Ignored ABI Changes: {lib_key}", level=2)
            print(f"{title}\n\n{result.details}\n")

    return success


if __name__ == "__main__":
    sanity_check()

    args = get_parser().parse_args()

    if args.abidiff_suppressions:
        os.environ["LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE"] = (
            args.abidiff_suppressions
        )

    archive_directory = os.path.join(args.archive_directory_parent, "libabigail-tars")
    if args.archive_on_core:
        print(f"Creating archive directory {archive_directory}")
        os.makedirs(archive_directory)

    abi_compatible = compare_tree_abis(
        args.old,
        args.new,
        args.suppressions,
        args.forward_compatible,
        args.archive_on_core,
        archive_directory,
        args.full_abi_diff,
    )

    if abi_compatible:
        print(
            format_title(
                f"Hurray! {args.old} and {args.new} are ABI-compatible!", level=2
            )
        )
    else:
        print(
            format_title(f"{args.old} and {args.new} are ABI-incompatible!", level=2),
            file=sys.stderr,
        )

    returncode = 0 if abi_compatible else 1
    sys.exit(returncode)
