import os
from pathlib import Path
from pprint import pprint as pp
import sys

#from file_utils import #project_dir #, write_tree_to_file, load_file_list
# from file_scan import ExtendedPath

class ExtendedPath(Path):
    def __new__(cls, *args):
        return super().__new__(cls, *args)
    
    def __init__(self, *args):
        super().__init__(*args)
        self.stats = self.drive

  
cwd = os.getcwd()
print("1. os.getcwd():  ", cwd)

p = Path(cwd)
print("2. Path(cwd):    ", p)

ep = ExtendedPath(p)
print("3. ExtendedPath: ", ep)
print("4. str():        ", str(ep))


print(sys.version)




