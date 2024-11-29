#!/usr/bin/env python3
# Written by MRDGH2821 <ask.mrdgh2821@outlook.com>
# This code is licensed under the MIT license.


import os
import re
import sys


def extract_latest_changelog(folder_path):
    changelog_file_path = os.path.join(folder_path, "CHANGELOG.md")
    with open(changelog_file_path, "r") as f:
        content = f.read()

    # Find the latest version header
    latest_version_header = re.search(r"^## v\d+\.\d+\.\d+$", content, re.MULTILINE)
    if latest_version_header:
        latest_version_header = latest_version_header.group()
        # Find the section corresponding to the latest version
        section = re.search(
            rf"{latest_version_header}(.*?)(?=^##|\Z)",
            content,
            re.DOTALL | re.MULTILINE | re.S,
        )
        if section:
            return section.group(0).strip()
    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_changelog.py <folder_name>")
        sys.exit(1)

    folder_name = sys.argv[1]
    folder_path = os.path.join(os.getcwd(), folder_name)

    if not os.path.exists(folder_path):
        print(f"Folder '{folder_name}' not found.")
        sys.exit(1)

    latest_changelog = extract_latest_changelog(folder_path)
    if latest_changelog:
        print(latest_changelog)
    else:
        print("No latest changelog found.")
