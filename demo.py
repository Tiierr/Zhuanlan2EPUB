#!/usr/bin/env python
import os

print os.getcwd()

os.chdir('papers')
print os.getcwd()

os.chdir("..")
print os.getcwd()
