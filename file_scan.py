import itertools
import logging
import pathlib
from pathlib import Path, PurePosixPath, PureWindowsPath
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

def xxh3_64(file: Path) -> str:
    hasher = xxhash.xxh3_64()
    with open(file=file, mode='rb',) as f:
        while chunk := (f.read(CHUNK_SIZE)):
            hasher.update(chunk)
        file_hash = hasher.hexdigest()
        hasher.reset()
        return file_hash

# Extend pathlib.Path functionality
class ExtendedPath(Path):
    def __new__(cls, *args):
        return super().__new__(cls, *args)

    def __init__(self, *args):
        super().__init__(*args)
        log.debug('initializeing extendedpath: windows=%s posix=%s', isinstance(self, PureWindowsPath), isinstance(self, PurePosixPath))
        _stat = self.stat()
        self.size = _stat.st_size
        self.modified = _stat.st_mtime
        self.created = _stat.st_birthtime \
            if hasattr(self, 'st_birthtime') \
            else _stat.st_ctime # Accounts for weird windows quirk where birthtime is used
        # self._created = _stat.st_ctime
        self.hard_links = _stat.st_nlink
        
        _attributes = {
            self.size
        }
        logging.debug('size=%(size)d | modified=%(modified)d | created=%(created)d | hard_links=%(hard_links)i',
                         {
                          'size':self.size, 
                          'modified':self.modified, 
                          'created':self.created, 
                          'hard_links':self.hard_links,
                          })
        

    
    @property    
    def depth(self) -> int:
        '''
        Equal to the depth below the root directory (root depth=0)
        
        Examples:   
        "/etc/hosts" -> depth=2  
        "/home/username/images/sample1.tiff" -> depth=4
        '''
        return len(self.parts)
    
    @property
    def file_type(self):
        log.debug('method: file_type | file: %s | suffix: %s', self.name, self.suffixes)
        return ''.join(self.suffixes)
    
    def as_string(self):
        return str(self)
    
    def file_hash(self) -> str:
        log.debug('hashing %s', str(self))

        hasher = xxhash.xxh3_64()
        
        try:
            with open(file=self, mode='rb',) as f:
                chunk_count = itertools.count()
                while chunk := (f.read(CHUNK_SIZE)):
                    next(chunk_count)
                    hasher.update(chunk)
                    log.debug('chunks_processed: %i', chunk_count)
            file_hash = hasher.hexdigest()
            log.debug('Chunks processed: %i | Hash: %s \nfile: %s', chunk_count, str(file_hash), str(self))
        except FileNotFoundError:
            log.warning('file %s not found', self.name)
            file_hash = ''
        finally:
            hasher.reset()
            log.debug('resetting hasher')
        
        return str(file_hash)
    
    def summary(self):
        _str = self.as_string()
        _hash = self.file_hash()
        _depth = self.depth
        _created = self.created
        _modified = self.modified
        
        f1 = f'file name: {_str}'
        f2 = f'file depth: {_depth}' 
        f3 = f'file hash: {_hash}'
        f4 = f'created: {_created}'
        f5 = f'modified: {_modified}'
        
        print(f1, f2, f3, f4, f5, sep='\n')
            
        
    

if __name__ == '__main__':
    ex = ExtendedPath(
        '/home/cdpacheco/Documents/GitHub'
        )
    print(
    ex.created
    )
    print(
    time.localtime(ex.modified)
    )
    
    
