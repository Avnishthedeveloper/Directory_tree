## tree structure with diff. color for files and directories and additional parameter for level of tree

from pathlib import Path
from itertools import islice
from colorama import Fore, Back, Style
import argparse

space =  '    '
branch = '│   '
tee =    '├── '
last =   '└── '

def tree(dir_path: Path, level: int=-1, limit_to_directories: bool=False,
         length_limit: int=1000):
    """Given a directory Path object print a visual tree structure"""
    dir_path = Path(dir_path) # accept string coerceable to Path
    files = 0
    directories = 0
    def inner(dir_path: Path, prefix: str='', level=-1):
        nonlocal files, directories
        if not level: 
            return # 0, stop iterating
        if limit_to_directories:
            contents = [d for d in dir_path.iterdir() if d.is_dir()]
        else: 
            contents = list(dir_path.iterdir())
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield (Fore.YELLOW+ prefix + pointer) + (Fore.RED + path.name)
                directories += 1
                extension = branch if pointer == tee else space 
                yield from inner(path, prefix=prefix+extension, level=level-1)
            elif not limit_to_directories:
                yield (Fore.BLUE+ prefix + pointer)+ (Fore.GREEN + path.name)
                files += 1
    print(dir_path.name)
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        print(line)
    if next(iterator, None):
        print(f'... length_limit, {length_limit}, reached, counted:')
    print(f'\n{directories} directories' + (f', {files} files' if files else ''))

if __name__ == '__main__':

	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-d", "--dir_path", type=str, help="base directory path for the tree")
	ap.add_argument("-l", "--level", type=int, help="level of the tree")
	ap.add_argument("-ld", "--limit_to_directories", type=bool, default=False,
		help="limit_to_directories")
	ap.add_argument("-ll", "--length_limit", type=int, default=1000, help="length_limit")
	# args = vars(ap.parse_args())
	args = ap.parse_args()

	if not args.dir_path:
		print('Directory path not found')
	else:
		tree(dir_path=args.dir_path, level=args.level, limit_to_directories=args.limit_to_directories,
         length_limit=args.length_limit)
