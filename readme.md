# Project Name

- Python Scripting Project

## Description

This project implements an automation system that performs the following tasks:

1. Scans a specified folder for Java and Golang files.
2. Creates corresponding folders for each programming language (Java and Golang) in a designated destination.
3. Copies the identified files into their respective language folders.
4. Compiles the source code files using language-specific compilation commands.

## Requirements

- Python 3.x
- Operating System: Linux/Unix. Windows, or Mac

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Belal-Mohsen/python_scripting_project.git

   ```

2. Navigate to the project directory:

   ```bash
   cd python_scripting_project

   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line with the following syntax:

```bash
python3 python_scripting_project.py source_directory destination_directory
```

- `source_directory`: The path to the directory containing Java and Golang files.
- `destination_directory`: The path where the project will create language-specific folders and compile the files.

## Example

```bash
python3 python_scripting_project.py Apps CompiledApps
```
