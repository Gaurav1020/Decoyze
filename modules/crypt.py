import sys
import hashlib


def summd5(file_path):
    # Calculate the MD5 hash of a file.
    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

def sumsha1(file_path):
    # Calculate the MD5 hash of a file.
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha1()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

def sumsha256(file_path):
    # Calculate the MD5 hash of a file.
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

