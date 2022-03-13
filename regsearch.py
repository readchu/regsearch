"""Prints lines and filenames of all files in provided directory that match
the provided regular expression.

Functions:
    user_directory
    regex_searcher
"""

import re
import PyInputPlus as pyip
from pathlib import Path

def folder_exists(folder_name: str) -> Optional[Path]:
"""Search all user directories for a folder and asks user to pick if multiple exist."""
    home_directory = Path.home()
    folder_holder = list(home_directory.rglob(folder_name))
    folder = None
    if len(folder_holder) == 1:
        folder = folder_holder[0]
    else:
        for i, WindowsPath in enumerate(folder_holder):
            folder_holder[i] = str(WindowsPath)
        #pyip,inputMenu only accepts strings and returns strings
        print("You have multiple folders with that name. Choose one of them. Tip: Use the numbers.\n")
        folder_as_str = pyip.inputMenu(folder_holder, numbered=True)
        folder = Path(folder_as_str)
    return folder

def regex_searcher():
"""TODO: Function for, with provided WindowsPath and regular expression,
returns dictionary with keys being the filenames of all files that matched
and values being lists of all lines that were in said files with matching expression
with line number... Match #X, Line Y: Line text
"""

if __name__ = "__main__":
