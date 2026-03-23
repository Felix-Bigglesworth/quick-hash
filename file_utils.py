
from pathlib import Path, PurePosixPath, PureWindowsPath
import pathlib
from dataclasses import dataclass

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

# def root_drive(Path):
#     pure_path = pathlib.PurePath(Path)
#     _drive, _root = (pure_path.drive, pure_path.root)
#     return ''.join([_drive, _root])

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


# The 10 elements always present are st_mode, st_ino, st_dev, st_nlink,
# st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime.

def getstats(fpath:Path):
    # format the Path.lstat() return value to a dictionary
    s = fpath.lstat()
    stat = {
        'st_mode': s.st_mode,
        'st_ino': s.st_ino,
        'st_dev': s.st_dev,
        'st_nlink': s.st_nlink,
        'st_uid': s.st_uid,
        'st_gid': s.st_gid,
        'st_size': s.st_size,
        'st_atime': s.st_atime,
        'st_mtime': s.st_mtime,
        'st_ctime': s.st_ctime,
        'st_birthtime': s.st_birthtime
    }
    return stat
    
    
    

@dataclass
class FileStats:
    st_mode: int        # file type and file mode bits (permissions)
    st_ino: int         # Unix:inode; Windows=fileindex (each file on a st_dev has a unique value)
    st_dev: int         # indentifier for the device a file resides on
    st_nlink: int       # Number of hard links
    st_uid: int         # User identifier (file owner)
    st_gid: int         # Group identifier (file owner)
    st_size: int        # file size in bytes (for a symlink its the size of the pathname it contains)
    st_atime: float     # time of most recent access (in seconds)
    st_mtime: float     # time of most recent content modification
    st_ctime: float     # Unix: time of the most recent metadata change; Windows:depricated
    st_birthtime: float # Time of file creation
    
    # # Unix only:
    # st_blocks: float
    # st_blksize: float
    
    # # On windows: 
    # st_file_attributes: None
    # st_reparse_tag: None
    