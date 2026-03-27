from pathlib import Path
import file_scan
from file_scan import ExtendedPath, walk_directory
from constants import CHUNK_SIZE, KILOBYTE, MEGABYTE, KB, MB
import time
import itertools
import logging

logging.basicConfig(
    level=logging.DEBUG,                                   # Minimum level to capture
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),                           # Print to console
        logging.FileHandler("my_script.log"),     # Also write to file
    ]
)
log = logging.getLogger(__name__)

ROOT_DIRECTORY = Path(r'\\platinum\e')
OUTPUT = Path('test_output.txt')

def main():
    START_TIME = time.perf_counter()
    FILE_HASHES = list()
    _counter = itertools.count()
    for _path in walk_directory(start=ROOT_DIRECTORY):
        _count = next(_counter)
        _node = ExtendedPath(_path)
        if not _node.is_file():
            continue
        _hash = _node.file_hash()
        _depth = _node.depth
        info = ' '.join((_hash, str(_depth), _node.as_string(), '\n'))
        
        FILE_HASHES.append(info)
    if OUTPUT.exists():
        mode = 'w'
    else:
        mode = 'x'
    with open(OUTPUT, mode=mode) as f:
        f.writelines(FILE_HASHES)
    END_TIME = time.perf_counter()
    print(f'{END_TIME - START_TIME} SECONDS')
    


if __name__ == "__main__":
    main()
