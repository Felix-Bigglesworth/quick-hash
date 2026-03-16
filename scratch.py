from pathlib import Path
from pprint import pprint as pp

from file_utils import write_tree_to_file, load_file_list


# root_dir = Path(r'/home/cdpacheco/Documents')
# file_list = root_dir.rglob('**')
# _dirs = [str(f) +'\n' for f in file_list]

# outfile = Path('./dir_tree.txt')
# with open(outfile, mode='x') as f:
#     f.writelines(_dirs)
    
# def append_newlines_list(lines: list[Path]):
#     # append a \n character to each list entry
#     return [str(f) + '\n' for f in lines]
    
# def dir_tree_to_file(root_dir, outfile:Path):
#     # rglob directory tree search
#     file_list = root_dir.rglob('**')
#     file_list = append_newlines_list(file_list)
    
#     mode = 'w' if outfile.exists() else 'x'
#     with open(file=outfile, mode=mode) as fhandle:
#         fhandle.writelines(file_list)
    
# write_tree_to_file(Path(r"F:\_dummy_data"), Path('./windows_dir_tree.txt'))
file_tree = Path(r'C:\Users\cdpacheco\github-desktop\quick-hash\windows_dir_tree.txt')
files = load_file_list(file_tree)

def strip_root():
    pass

def strip_drive():
    # for windows paths
    pass
