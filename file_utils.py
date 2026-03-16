
from pathlib import Path, PurePosixPath, PureWindowsPath
import pathlib

# WRITE FILES

def append_newlines_list(lines: list[Path]):
    # append a \n character to each list entry
    return [str(f) + '\n' for f in lines]
    
def write_tree_to_file(root_dir:Path, outfile:Path):
    # rglob directory tree search
    print('scanning root directory:', str(root_dir))
    print('outfile:', str(outfile))
    file_list = root_dir.rglob('**')
    file_list = append_newlines_list(file_list)
    
    mode = 'w' if outfile.exists() else 'x'
    with open(file=outfile, mode=mode) as fhandle:
        fhandle.writelines(file_list)


# READ FILES

def load_file_list(fpath:Path, os_type=None):
    with open(file=fpath,mode='r') as handle:
        lines = [str_to_path(line, _type=os_type) for line in handle.readlines()]
    return lines

def str_to_path(string:str, _type):
    string = string.strip()
    # Override os autodetection to work directly with the desired path
    match _type:
        case 'posix':
            asPath = PurePosixPath(string)
        case 'windows':
            asPath = PureWindowsPath(string)
        case _ :
            asPath = Path(string)
        
    return asPath


# FORMATTING

def root_drive(Path):
    pure_path = pathlib.PurePath(Path)
    _drive, _root = (pure_path.drive, pure_path.root)
    return ''.join([_drive, _root])

def file_depth(file_path: pathlib.PurePath):
    file_path.parts()
    

# ==== FILE DATA ====
# https://docs.python.org/3/library/os.html#os.stat_result
# 
# Path.stat() -> Stat object with file metadata (last change)
# === stat attributes ===
# st_ino: unique file identity for a given device id unix:inode win:file_index
# st_dev: device identifier
# st_nlink: # of hard links
# st_uid: File owner User identifier
# st_gid: File owner Group identifier
# st_size: size of file in bytes (sym-links its the len of the pathname)
# === Timestamps ===
# --- In seconds ---
# st_atime: last accessed
# st_mtime: last modified
# st_ctime: metadata last changed (depricated on windows)
# st_birthtime: windows ctime  
# --- In Nanoseconds ---
# st_atime_ns
# st_mtime_ns
# st_ctime_ns
# st_birthtime_ns
# === On some unix systems ===
# st_blocks
# st_blksize
# st_rdev
# *st_type
