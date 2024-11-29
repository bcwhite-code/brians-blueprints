#!/usr/bin/env python3
# Written by MRDGH2821 <ask.mrdgh2821@outlook.com>
# This code is licensed under the MIT license.


import os
import re
import sys


def extract_changelog(folder_path, version):
    changelog_file_path = os.path.join(folder_path, "CHANGELOG.md")
    with open(changelog_file_path, "r") as f:
        content = f.read()

    # Find the section corresponding to the version
    section = re.search(
        rf"^## v{version}(.*?)(?=^##|\Z)",
        content,
        re.DOTALL | re.MULTILINE | re.S,
    )
    if section:
        return section.group(0).strip()
    return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 extract_changelog.py <folder_name> <version>")
        sys.exit(1)

    folder_name = sys.argv[1]
    version = sys.argv[2]

    folder_path = os.path.join(os.getcwd(), folder_name)

    if not os.path.exists(folder_path):
        print(f"Folder '{folder_name}' not found.")
        sys.exit(1)

    changelog = extract_changelog(folder_path, version)
    if changelog:
        print(changelog)
    else:
        print(f"No changelog found for version {version}.")
