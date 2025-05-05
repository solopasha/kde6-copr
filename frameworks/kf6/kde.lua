local kde_maps = require "fedora.srpm.kde_maps"

local source_urls = {
    ["frameworks"] =
    "https://download.kde.org/%{stable_kf6}/frameworks/%{maj_ver_kf6}.%{min_ver_kf6}/%{framework}-%{version}.tar.xz",
    ["plasma"] =
    "https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{base_name}-%{version}.tar.xz",
    ["gear"] =
    "https://download.kde.org/%{stable_kf6}/release-service/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/src/%{base_name}-%{version}.tar.xz",
    ["git"] =
    "https://invent.kde.org/%{name2name_with_namespace}/-/archive/%{commit0}/%{base_name}-%{shortcommit0}.tar.gz",
}

local source_urls_mt = {}

source_urls_mt.__call = function(table, name, namespace)
    if table[name] then
        return table[name]
    elseif table[namespace] then
        return table[namespace]
    else
        return "https://download.kde.org/%{stable_kf6}/%{base_name}/%{base_name}-%{version}.tar.xz"
    end
end

setmetatable(source_urls, source_urls_mt)

function kde_maps:name2name_with_namespace(name)
    return self[name]
end

function kde_maps:name2namespace(name)
    if not self[name] then
        rpm.expand("%{error:namespace for " .. name .. " not found!}")
    end
    local kde_gear = require "fedora.srpm.kde_gear"
    if kde_gear[name] then
        return "gear"
    end
    local namespace = self[name]:gsub("/.*", "")
    return namespace
end

local actions = {}

function kde_maps:source_url(name, namespace, is_git)
    if not self[name] then
        rpm.expand("%{error:" .. name .. " not found!}")
    end
    local source

    if is_git then
        source = rpm.expand("Source0:   " ..
            source_urls("git"):gsub("%%{name2name_with_namespace}", self:name2name_with_namespace(name)) .. "\n")
        macros.sourcerootdir = rpm.expand(name .. "-%{commit}")
    else
        source = "Source0: " .. rpm.expand(source_urls(name, namespace)) .. "\n" ..
            "Source1: " .. rpm.expand(source_urls(name, namespace)) .. ".sig\n" ..
            "Source2: signing-key.pgp\n"
        macros.sourcerootdir = rpm.expand(name .. "-%{version}")
    end
    return source
end

function actions:common(base_name, is_noarch)
    self.namespace = kde_maps:name2namespace(base_name)
    macros.base_name = base_name

    if self[base_name] then
        self[base_name](self)
    elseif self[self.namespace] then
        self[self.namespace](self)
    end

    print(kde_maps:source_url(base_name, self.namespace, (macros.bumpver or macros.gitdate)))

    if macros._kf6_build_qch == "1" then
        print("BuildRequires:  doxygen\n")
        print("BuildRequires:  qt6-doc-devel\n")
    end

    if macros.name ~= "extra-cmake-modules" then
        print("BuildRequires:  extra-cmake-modules\n")
    end

    if not is_noarch then
        print("BuildRequires:  gcc-c++\n")
    end

    print("BuildRequires:  cmake\n")
    print("BuildRequires:  kf6-rpm-macros\n")
end

function actions:frameworks()
    self.namespace = "frameworks"
    print("BuildSystem:    cmake_kf6\n")
    print("Requires:       kf6-filesystem\n")
end

function actions:plasma()
    self.namespace = "plasma"
    print("BuildSystem:    cmake_kf6\n")
end

function actions:spectacle()
    self:plasma()
end

local function meta(is_noarch)
    local fedora = require "fedora.common"
    fedora.zalias({ "commit", "shortcommit" }, false)
    local base_name = macros.framework or (macros.base_name or macros.name)
    actions:common(base_name, is_noarch)
end

return {
    meta = meta
}
