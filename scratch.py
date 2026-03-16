from pathlib import Path
from pprint import pprint as pp

root_dir = Path(r'/home/cdpacheco/Documents')
file_list = root_dir.rglob('**')
_dirs = [str(f) +'\n' for f in file_list]

outfile = Path('./dir_tree.txt')
with open(outfile, mode='x') as f:
    f.writelines(_dirs)
    

