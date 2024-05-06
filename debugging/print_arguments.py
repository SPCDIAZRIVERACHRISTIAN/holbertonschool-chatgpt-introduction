#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("No arguments provided.")
else:
    for i in range(len(sys.argv)):
        print(sys.argv[i])
