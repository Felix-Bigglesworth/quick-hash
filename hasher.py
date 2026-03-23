from pathlib import Path
import xxhash
from constants import CHUNK_SIZE

"""
The xxhash library has multiple options for hashing algorithms
xxhash32
xxhash64
xxh3_64
xxh3_128
"""


#TODO make sure large files are read in a byte stream
#TODO confirm the correct hash function is being used
#TODO confirm consistency of hashes compared to the linux xxhash library 
# when using `xxhsum -H3 ./file` command
def xxhash64(file) -> str:
    hash_factory = xxhash.xxh3_64()
    with open(file=file, mode='rb',) as f:
        while chunk := (f.read(CHUNK_SIZE)):
            hash_factory.update(chunk)
        file_hash = hash_factory.hexdigest()
        hash_factory.reset()
        return file_hash

if __name__ == '__main__':
    _hash1 = xxhash64(file=Path('./file_2.dat'))
    print(str(_hash1))
    
    # _hash2 = xxhash.xxh3_64_hexdigest(Path('./file_2.dat'))