import logging
import pathlib
from pathlib import Path
import os
from os import PathLike
import sys
from hasher import xxhash64
from pprint import pprint as pp
from dataclasses import dataclass
import xxhash
import time
from constants import CHUNK_SIZE

logging.basicConfig(
    level=logging.DEBUG,                          # Minimum level to capture
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),                  # Print to console
        logging.FileHandler("my_script.log"),     # Also write to file
    ]
)
log = logging.getLogger(__name__)

# PLATFORM = sys.platform # SYSTEM_OS: 'win32' or 'linux'
log.info('Platform=%s | Script: %s', __file__, sys.platform)



# Walking the filesystem can be done using either pathlib.Path.walk() or pathlib.path.rglob()
def walk_directory(start:Path):
    # recursively search the given directory for all subdirectories and files.
    # Note: includes the starting directory itself
    return start.rglob(pattern='**')

def xxh3(file: Path) -> str:
    hasher = xxhash.xxh3_64()
    with open(file=file, mode='rb',) as f:
        while chunk := (f.read(CHUNK_SIZE)):
            hasher.update(chunk)
        file_hash = hasher.hexdigest()
        hasher.reset()
        return file_hash

# Rename and inherit from pathlib.Path??    
class ExtendedPath(Path):
    def __new__(cls, *args):
        return super().__new__(cls, *args)
    
    def __init__(self, *args):
        super().__init__(*args)
        self.stats = self.drive
