from pathlib import Path
import os
import pathlib
from dataclasses import dataclass

fpath = Path('dir_tree.txt')
with open(fpath, mode='r') as f:
    data: list[Path] = [Path(dat) for dat in f.readlines()]
    
@dataclass
class File:
    path: pathlib.Path
    root: pathlib.Path

Files = [File(dat, dat.root) for dat in data]

print(Files)

