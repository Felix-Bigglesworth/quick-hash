from pathlib import Path
import os
import pathlib
from dataclasses import dataclass

fpath = Path('dir_tree.txt')
with open(fpath, mode='r') as f:
    data: list[Path] = [Path(dat) for dat in f.readlines()]
    


def read_file_list(fpath:Path):
    with open(file=fpath,mode='r') as handle:
        lines = [str.strip(line) for line in handle.readlines()]
    return lines
        