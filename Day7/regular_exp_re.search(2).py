import re
# This script reads a file and prints lines that start with 'From: '
file=input('enter file name: ')
try:
    fhand= open(file)
except:
    print('File cannot be opened:', file)
    exit()

for line in fhand:
    line = line.rstrip()
    if re.search('^From: ',line):
        print(line)
