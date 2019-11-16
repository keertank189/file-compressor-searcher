#!/usr/bin/python
import os
from os.path import join, abspath, isfile, isdir, exists, basename
import sys
import fmindex

def main():
    if not len(sys.argv) in [3]:
        print('Usage: ')
        print('  %s data index' % sys.argv[0])
        os.abort()
    else:
        if not isfile(sys.argv[1]):
            print("Input file doesn't exist")
            os.abort()
        inp=open(sys.argv[1])
        data=inp.read()
        idx=fmindex.index(data)
        fmindex.save(sys.argv[2], idx)
if __name__ == '__main__':
    main()