from pathlib import Path
from os import PathLike
import os
import sys
import pathlib
from pprint import pprint as pp
from hasher import xxhash64
from pprint import pprint
from dataclasses import dataclass

# PLATFORM = sys.platform # Windows: 'win32'; Linux: 'linux'
# drive = Path(os.getcwd()).resolve()
# print(drive)

# Adds the to_str method to pathlib.Path objects
# replace with `Path.__str__()` ?
# def to_str(self):
#     return str(self)
# Path.to_str = to_str

# Walking the filesystem can be done using either pathlib.Path.walk() or pathlib.path.rglob()
def walk_directory(start:Path) -> os.Iterator[Path]:
    # recursively search the given directory for all subdirectories and files.
    # Note: includes the starting directory itself
    return start.rglob(pattern='**')


# Rename and inherit from pathlib.Path??    
class ExtendedPath(Path):
    def __new__(cls, *args):
        return super().__new__(cls, *args)
    
    def __init__(self, *args):
        super().__init__(*args)
        self.stats = self.drive
