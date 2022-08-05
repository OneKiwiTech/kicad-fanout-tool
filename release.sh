#!/bin/bash -e

version=$(git describe --tags --dirty)
name=$(echo edit-multi-text-$version.zip)

echo "Building release $version"
cp metadata.json.template metadata.json
sed -i -e "s/VERSION/$version/g" metadata.json
sed -i '/download_/d' metadata.json
sed -i '/install_size/d' metadata.json

mkdir resources
cp icon/icon_64x64.png resources/
mv resources/icon_64x64.png resources/icon.png

mkdir plugins
cp __init__.py plugins/
cp icon.png plugins/
cp -r onekiwi/ plugins/

zip -r $name plugins resources metadata.json

rm -rf plugins
rm -rf resources

sha=$(sha256sum $name | cut -d' ' -f1)
size=$(du -b $name | cut -f1)
installSize=$(unzip -l $name | tail -1 | xargs | cut -d' ' -f1)

cp metadata.json.template metadata.json
sed -i -e "s/VERSION/$version/g" metadata.json
sed -i -e "s/SHA256/$sha/g" metadata.json
sed -i -e "s/DOWNLOAD_SIZE/$size/g" metadata.json
sed -i -e "s/INSTALL_SIZE/$installSize/g" metadata.json

ls -lh $name metadata.json

