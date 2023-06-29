#!/usr/bin/python

import os
import shutil
import re
from obsidian_to_hugo import ObsidianToHugo

content_path = './hugo/content'
shutil.rmtree(content_path)
os.mkdir(content_path)

def filter_file(file_contents: str, file_path: str) -> bool:
    if "draft:: false" in file_contents:
        print(file_path, file_contents);
        return True # copy file
    else:
        return False # skip file

def remove_comment(file_contents: str) -> str:
    return re.sub(r"%%.*?%%", "", file_contents, flags=re.DOTALL)

obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir="./notes",
    hugo_content_dir=content_path,
    filters=[filter_file],
    processors=[remove_comment],
)

obsidian_to_hugo.run()
