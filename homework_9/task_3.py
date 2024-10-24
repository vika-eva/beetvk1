import os
import sys

name = input("Enter file name: ")

def count_lines(name):
    with open(name, "r+") as file:
        lines = file.readlines()
        total_lines = len(lines)
    return total_lines
#print(count_lines(name))

def count_chars(name):
    with open(name, "r+") as file:
        content = file.read()
        total_chars = len(content)
        return total_chars
#print(count_chars(name))

def test():
    count_lines(name)
    count_chars(name)
print(count_lines(name), count_chars(name))

