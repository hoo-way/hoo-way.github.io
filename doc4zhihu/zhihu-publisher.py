

# Usage: This program aims to transfer your markdown file into a way zhihu.com can recognize correctly.
#        It will mainly deal with your local images and the formulas inside.

import os, re
import argparse
import codecs
import subprocess
import chardet
import functools

from PIL import Image
from pathlib2 import Path
from shutil import copyfile

###############################################################################################################
## Please change the GITHUB_REPO_PREFIX value according to your own GitHub user name and relative directory. ##
###############################################################################################################
# GITHUB_REPO_PREFIX = Path("https://raw.githubusercontent.com/`YourUserName`/`YourRepoName`/master/Data/")
GITHUB_REPO_PREFIX = "(https://hoo-way.github.io/data/" # Your image folder remote link 
COMPRESS_THRESHOLD = 5e5 # The threshold of compression

# The main function for this program
def process_for_zhihu():
    with open(str(args.input), 'rb') as f:
        print(str(args.input))
        s = f.read()
        chatest = chardet.detect(s)
    print(chatest)
    with open(str(args.input),"r",encoding=chatest["encoding"]) as f:
        lines = f.read()
        lines = image_ops(lines)
        with open(args.input.parent/(args.input.stem+"_for_zhihu.md"), "w+", encoding=chatest["encoding"]) as fw:
            fw.write(lines)
        git_ops()


# The support function for image_ops. It will take in a matched object and make sure they are competible
def rename_image_ref(m, original=True):
    global image_folder_path
    image_path = re.sub("./","",os.path.dirname (m.group(2) ))
    # print(os.path.dirname (m.group(2) ))
    # print(image_folder_path.name)
    # if not Path(m.group(1)).is_file():
    #     return m.group(0)

    image_ref_name = Path(m.group(2)).name

    return "!["+m.group(2)+"]("+GITHUB_REPO_PREFIX+str(image_path)+"/"+image_ref_name+")"



# Search for the image links which appear in the markdown file. It can handle two types: ![]() and <img src="LINK" alt="CAPTION" style="zoom:40%;" />.
# The second type is mainly for those images which have been zoomed.
def image_ops(_lines):
    # if args.compress:
    #     _lines = re.sub(r"\!\[(.*?)\]\((.*?)\)",lambda m: "!["+m.group(1)+"]("+GITHUB_REPO_PREFIX+str(image_folder_path.name)+"/"+Path(m.group(2)).stem+".jpg)", _lines)
    #     _lines = re.sub(r'<img src="(.*?)"',lambda m:'<img src="'+GITHUB_REPO_PREFIX+str(image_folder_path.name)+"/"+Path(m.group(1)).stem+'.jpg"', _lines)
    # else:
    _lines = re.sub(r"\!\[(.*?)\]\((.*?)\)",functools.partial(rename_image_ref, original=True), _lines)
    _lines = re.sub(r'<img src="(.*?)"',functools.partial(rename_image_ref, original=False), _lines)
    return _lines

# Push your new change to github remote end
def git_ops():
    subprocess.run(["git","add","-A"])
    subprocess.run(["git","commit","-m", "update file "+args.input.stem])
    subprocess.run(["git","push", "-u", "origin", "master"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Please input the file path you want to transfer using --input=""')

    # RGB arguments
    parser.add_argument(
        '--compress', action='store_true', help='Compress the image which is too large')

    parser.add_argument(
        '--input',
        type=str,
        help='Path to the file you want to transfer.')

    args = parser.parse_args()
    if args.input is None:
        raise FileNotFoundError("Please input the file's path to start!")
    else:
        args.input = Path(args.input)
        image_folder_path = args.input.parent/(args.input.stem)
        print(image_folder_path.name)
        process_for_zhihu()