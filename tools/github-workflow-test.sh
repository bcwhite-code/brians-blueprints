#!/usr/bin/env bash

GITHUB_REF="self-building-factory-5.0.0"

echo github_ref=$GITHUB_REF
folder=${GITHUB_REF#*/tags/}
folder=${folder%-*}
version=${GITHUB_REF##*/}
version=${version//[!0-9.]/}

release_name=$(echo "${folder//-/ }" | sed -e "s/\b\(.\)/\u\1/g;s/Brians/Brian's/g")
release_name="$release_name $version"

echo "folder=$folder"
echo "version=$version"
echo "release_name=$release_name"
