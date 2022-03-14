"""Prints lines and filenames of all basic text files in provided directory that match
the provided regular expression.

Functions:
    folder_exists(str) -> Path | bool
    regex_finder(re object, Path) -> dict

#TODO: Search PDFs, search Word docs, etc. https://automatetheboringstuff.com/2e/chapter15/
"""
import logging
import pprint
import re
from pathlib import Path
from typing import Union

import pyinputplus as pyip

logging.basicConfig(
    filename="regsearch_DEBUG.txt",
    level=logging.DEBUG,
    format=" %(asctime)s - %(levelname)s - %(message)s",
)
logging.disable(logging.CRITICAL)


def folder_exists(folder_name: str) -> Union[Path, bool]:
    """Search all user directories for a folder and asks user to pick if multiple exist."""
    home_directory = Path.home()
    name_results = list(home_directory.rglob(folder_name))
    folder_holder = []
    folder_path = False
    #pyip,inputMenu only accepts strings and returns strings
    for i, windows_path in enumerate(name_results):
        if windows_path.is_dir():
            folder_holder.append(str(windows_path))
    if not folder_holder:
        pass
    elif len(folder_holder) == 1:
        folder_path = Path(folder_holder[0])
    else:
        print("You have multiple folders with that name. Choose one of them. Tip: Use the numbers.\n")
        folder_path = Path(pyip.inputMenu(folder_holder, numbered=True))
    return folder_path

def regex_finder(regex, directory: Path) -> dict:
    """Return all lines that match the regex from basic text files in directory.

    Output is a dictionary with keys being the filenames of all files with matching
    lines and values being lists of of those lines in the following format:
        Match #X, Line Y: <Line Text>
    """
    all_files = directory.glob("*.*")
    matching_files = {}
    for file in all_files:
        try:
            with open(file, 'r', errors="ignore") as f:
                #there's a UnicodeDecodeError that's popping up which I'm not sure how to resolve...
                #just gonna silence the errors...
                all_lines = f.readlines()
                for line in all_lines:
                    if regex.search(line):
                        matching_files.setdefault(file.name, [])
                        matched_file = matching_files[file.name]
                        match_num = str(len(matched_file) + 1)
                        line_num = str(all_lines.index(line))
                        entry = f"Match #{match_num}, Line {line_num}: {line}"
                        matched_file.append(entry)
        except PermissionError:
            print(f"You do not have permission to access {file.name}. Going to next file...\n")
    return matching_files

if __name__ == "__main__":
    """Query user for a folder, check if the folder exists, ask them for another folder if it doesn't.
    When a folder exists, ask them for a regular expression.
    call regex_finder
    print out dictionary
    """

    folder_found = False
    while not folder_found:
        folder = input("Please enter the name of the folder you want to search:\n")
        folder_found = folder_exists(folder)
        if not folder_found:
            print(f"{folder} does not exist in your home directory, unfortunately.\n")

    regex = pyip.inputRegexStr("Please enter a regular expression to search for: \n")

    matches = regex_finder(regex, folder_found)

    pprint.pprint(matches)
