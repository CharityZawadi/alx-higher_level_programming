#!/usr/bin/python3
import string
__import__('os').write(1, bytes(getattr(string, 'ascii_uppercase', string.ascii_letters), 'utf-8') + b'\n')

