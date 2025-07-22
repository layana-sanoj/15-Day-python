#getting email addresses from a file using regular expressions
#This code reads a file and extracts email addresses from lines that start with 'From'
import re

file='mbox.txt'
fhand=open(file)
 
for line in fhand:
    line=line.rstrip()
    if  re.findall('^From (\S+@\S+)', line):
        print(re.findall('^From (\S+@\S+)', line))
