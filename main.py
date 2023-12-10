import os
import json
import shutil
from subprocess import PIPE, run
import sys

DIR_JAVA = "java"
DIR_GO = "go"


def get_all_apps_dirs(source):
    java_apps_paths = []
    go_apps_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if DIR_JAVA in directory.lower():
                java_apps_paths.append(os.path.join(source, directory))
            elif DIR_GO in directory.lower():
                go_apps_paths.append(os.path.join(source, directory))
        break
    return java_apps_paths, go_apps_paths


def main(source, dest):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    dest_path = os.path.join(cwd, dest)
    java_paths, go_paths = get_all_apps_dirs(source_path)
    print(java_paths, "\n", go_paths)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must enter source and destination directories!")
    source, dest = args[1:]
    main(source, dest)
