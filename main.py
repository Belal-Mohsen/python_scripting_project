import os
import json
import shutil
from subprocess import PIPE, run
import sys

DIR_JAVA = "java"
DIR_GO = "go"
GO_FILE_EXTENSION = ".go"
JAVA_FILE_EXTENSION = ".java"
GO_COMPILE_COMMAND = ["go", "build"]
JAVA_COMPILE_COMMAND = ["javac"]


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


def copy_files_and_compile(paths, dir_names, dest_path, sub_dir_name, compile_instr, file_extension):
    for source, dest in zip(paths, dir_names):
        output_dest_path = os.path.join(
            dest_path, sub_dir_name.capitalize(), dest)

        copy(source, output_dest_path)
        compile_code(output_dest_path, compile_instr, file_extension)


def compile_code(path, compile_instr, file_extension):
    source_code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_extension):
                source_code_file_name = file
                break
        break

    if source_code_file_name is None:
        return
    command = compile_instr + [source_code_file_name]
    run_cmd(command, path)


def run_cmd(command, path):
    cwd = os.getcwd()
    os.chdir(path)
    output = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    os.chdir(cwd)


def main(source, dest):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    dest_path = os.path.join(cwd, dest)
    #
    java_paths, go_paths = get_all_apps_dirs(source_path)
    create_dirs(dest_path, DIR_JAVA)
    create_dirs(dest_path, DIR_GO)
    java_apps_names = get_apps_name(java_paths, "_Java")
    go_apps_names = get_apps_name(go_paths, "_Go")
    copy_files_and_compile(java_paths, java_apps_names, dest_path,
                           DIR_JAVA, JAVA_COMPILE_COMMAND, JAVA_FILE_EXTENSION)
    copy_files_and_compile(go_paths, go_apps_names, dest_path,
                           DIR_GO, GO_COMPILE_COMMAND, GO_FILE_EXTENSION)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must enter source and destination directories!")
    source, dest = args[1:]
    main(source, dest)
