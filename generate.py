#!/usr/bin/python

import os
import shutil
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

obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir=".",
    hugo_content_dir=content_path,
    filters=[filter_file],
)

obsidian_to_hugo.run()
