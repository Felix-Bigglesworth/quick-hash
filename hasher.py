from pathlib import Path
import xxhash

file = Path('test1.dat')

algo = xxhash.xxh128()
# outputs a file hash
with open(file, mode='rb') as f:
    chunk = f.read()
    algo.update(chunk)
    out = algo.hexdigest()

print(out)