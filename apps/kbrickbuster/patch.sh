#! /usr/bin/env bash
# This script is used to rename/modified whatever is needed to be able to
# release kbreakout in Fedora as kbrickbuster

orig_tarball="$1"
orig_basename="$(basename "$orig_tarball")"
base_dir=${orig_basename%*.tar.xz}
base_version="${base_dir#kbreakout-}"
out_dir=$(mktemp -d /tmp/output.XXXXXXXXXX) || { echo "Failed to create temp file"; exit 1; }

tar Jxf "$orig_tarball" -C "$out_dir"
pushd "$out_dir" || exit 1
find "${base_dir}/" \! \( -name "*.svgz" -prune \) -type f -exec sed -i -e "s|&kbreakout;|KBrickbuster|g" {} \;
find "${base_dir}/" \! \( -name "*.svgz" -prune \) -type f -exec sed -i -e "s|kbreakout|kbrickbuster|g" {} \;
find "${base_dir}/" \! \( -name "*.svgz" -prune \) -type f -exec sed -i -e "s|KBreakout|KBrickbuster|g" {} \;
find "${base_dir}/" \! \( -name "*.svgz" -prune \) -type f -exec sed -i -e "s|Break[Oo]ut|Brickbuster|g" {} \;
find "${base_dir}/" \! \( -name "*.svgz" -prune \) -type f -exec sed -i -e "s|breakout|brickbuster|g" {} \;
find "${base_dir}/" \! \( -name "*.svgz" -prune \) -type f -exec sed -i -e "s|alienbreakout|alienbrickbuster|g" {} \;
find "${base_dir}/" \! \( -name "*.svgz" -prune \) -type f -exec sed -i -e "s|KBreakOut|KBrickbuster|g" {} \;

for f in 128 64 48 32 22 16 ; do 
  if [ -f "$base_dir/pics/$f-apps-kbreakout.png" ]; then
  mv "${base_dir}/pics/${f}-apps-kbreakout.png" "${base_dir}/pics/${f}-apps-kbrickbuster.png"
  fi
done

for lang in "${base_dir}"/po/* ; do
  mv "${lang}/kbreakout.po" "${lang}/kbrickbuster.po"
  if [ -d "$lang/docs/kbreakout" ] ; then
  mv "${lang}/docs/kbreakout" "${lang}/docs/kbrickbuster"
  fi
done

mv "${base_dir}/src/org.kde.kbreakout.desktop" "${base_dir}/src/org.kde.kbrickbuster.desktop"
mv "${base_dir}/src/org.kde.kbreakout.appdata.xml" "${base_dir}/src/org.kde.kbrickbuster.appdata.xml"
mv "${base_dir}/pics/sc-apps-kbreakout.svg" "${base_dir}/pics/sc-apps-kbrickbuster.svg"
mv "${base_dir}/themes/alienbreakout.desktop" "${base_dir}/themes/alienbrickbuster.desktop"
mv "${base_dir}/themes/alienbreakout.svg" "${base_dir}/themes/alienbrickbuster.svg"
mv "${base_dir}/themes/alienbreakout_preview.png" "${base_dir}/themes/alienbrickbuster_preview.png"
mv "${base_dir}/themes/egyptianbreakout_preview.png" "${base_dir}/themes/egyptianbrickbuster_preview.png"
mv "${base_dir}/themes/egyptianbreakout.svg" "${base_dir}/themes/egyptianbrickbuster.svg"
mv "${base_dir}/src/kbreakout.kcfg" "${base_dir}/src/kbrickbuster.kcfg"
mv "${base_dir}/src/kbreakout.qrc" "${base_dir}/src/kbrickbuster.qrc"
mv "${base_dir}/src/kbreakoutui.rc" "${base_dir}/src/kbrickbusterui.rc"
popd || exit 1

mv "$out_dir/$base_dir" "$out_dir/kbrickbuster-${base_version}"
pushd "$out_dir/" || exit 1
tar Jcf "/tmp/kbrickbuster-${base_version}.tar.xz" *
popd || exit 1
echo "/tmp/kbrickbuster-${base_version}.tar.xz is created."
rm -rf "$out_dir"
