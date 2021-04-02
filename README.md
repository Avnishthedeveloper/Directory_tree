# Directory_tree

# Install necessary libraries:

pip install -r requirements.txt

# Help options to run the cmd directory tree tool:

python3 tree.py -h

usage: tree.py [-h] [-d DIR_PATH] [-l LEVEL] [-ld LIMIT_TO_DIRECTORIES]
               [-ll LENGTH_LIMIT]

optional arguments:
  -h, --help            show this help message and exit
  -d DIR_PATH, --dir_path DIR_PATH
                        base directory path for the tree
  -l LEVEL, --level LEVEL
                        level of the tree
  -ld LIMIT_TO_DIRECTORIES, --limit_to_directories LIMIT_TO_DIRECTORIES
                        limit_to_directories
  -ll LENGTH_LIMIT, --length_limit LENGTH_LIMIT
                        length_limit

# Run

python3 tree.py -d <dir_path> -l <level>

# Example

python3 tree.py -d './' -l 2
