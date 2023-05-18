#!/usr/bin/python3
"""
Main file for testing
"""

validUtf8 = __import__('0-validate_utf8').validUtf8

data = [65]
print(validUtf8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUtf8(data))

data = [229, 65, 127, 256]
print(validUtf8(data))