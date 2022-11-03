
# This script generates a SHA256 hash from a json file

import hashlib as hs
import os
import sys


def append_hashcode(hash, lines):
    with open("hash.txt", "w") as hash_file:
        for line in range(0, lines-1):
            hash_file.writelines(hash.hexdigest() + "\n")

# This function genrates hash for each json file
def create_hash_function(jsonfile):
    hash = hs.sha256()
    with open(jsonfile, 'rb') as f:
        for byteBlock in iter(lambda: f.read(4096), b""):
            hash.update(byteBlock)
            print(hash.hexdigest())
            append_hashcode(hash, 10)
            






def check_directory():
    # assign directory
    directory = 'jsonpath'
    # iterate over files in
    # that directory
    for file in os.listdir(directory):
        jsonfile = os.path.join(directory, file)
        # checking if it is a file
        if os.path.isfile(jsonfile):
            create_hash_function(jsonfile)
            # print(jsonfile)


if __name__ == '__main__':
    check_directory()