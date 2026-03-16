from pathlib import Path
import pathlib
from hasher import xxhash64
from pprint import pprint
from dataclasses import dataclass


root=r'F:\_dummy_data\recursive_file_tree' 
root=Path(root)

# @dataclass()
# class Directory:
#     _path: pathlib.Path
#     depth: int

pathlib.PurePosixPath





# Get a full file list
# outputs a legth=3 tuple with the following:

file_list = []

# add all files to a list while skipping directories
directory_tree = root.walk()
for path, _dirs, _files in directory_tree:
    for f in _files:
        file = path / f
        if file.exists():
            _hash = xxhash64(file)
        file_list.append((_hash, file.__str__()))

def walk_directory_tree


# hash_set = \
#     {_hash for _hash, _ in file_list}
# conType = type(hash_set)    
# print(len(hash_set))

# pprint(
#     {_hash for _hash, _ in file_list},
#     width=200
# )
