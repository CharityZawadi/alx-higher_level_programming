#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
print("{:d} argument{}{}"
      .format(argc, "s" if argc != 1 else "", ":" if argc else "."))

for i in range(argc):
    print("{:d}: {}".format(i + 1, argv[i + 1]))

