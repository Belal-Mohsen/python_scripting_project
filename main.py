import os
import json
import shutil
from subprocess import PIPE, run
import sys

DIR_JAVA = "java"
DIR_GO = "go"


def create_dirs(path, type):
    full_dir = os.path.join(path, type.capitalize())
    if not os.path.exists(full_dir):
        os.makedirs(full_dir)


def get_apps_name(paths, to_trim):
    names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_trim, "")
        names.append(new_dir_name)

    return names


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


def copy(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)


def copy_files(paths, dir_names, dest_path, sub_dir_name):
    for source, dest in zip(paths, dir_names):
        output_dest_path = os.path.join(
            dest_path, sub_dir_name.capitalize(), dest)
        print(output_dest_path)

        copy(source, output_dest_path)


def main(source, dest):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    dest_path = os.path.join(cwd, dest)
    java_paths, go_paths = get_all_apps_dirs(source_path)
    create_dirs(dest_path, DIR_JAVA)
    create_dirs(dest_path, DIR_GO)
    java_apps_names = get_apps_name(java_paths, "_Java")
    go_apps_names = get_apps_name(go_paths, "_Go")
    copy_files(java_paths, java_apps_names, dest_path, DIR_JAVA)
    copy_files(go_paths, go_apps_names, dest_path, DIR_GO)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must enter source and destination directories!")
    source, dest = args[1:]
    main(source, dest)
