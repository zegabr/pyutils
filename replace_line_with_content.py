"""
this script recieves 4 arguments: 
    F the file to be changed,
    LINE_PREFIX the prefix of the line that must be changed
    NEW_LINE the line to replace the line that has LINE_PREFIX as prefix    

you can use this to add line to a file or change a line that is already there
"""

import sys

FILE = sys.argv[1]
LINE_PREFIX = sys.argv[2]
NEW_LINE = sys.argv[3]

file_obj = open(FILE, 'r')
lines = file_obj.read().split('\n')
file_obj.close()

#find LINE and replace it
found = False
for i in range(len(lines)):
    if lines[i].startswith(LINE_PREFIX):
        lines[i] = NEW_LINE
        found = True
        break

if not found:
    lines.append(NEW_LINE)

#rewrite file
text = '\n'.join(lines)
file_obj = open(FILE, 'w')
file_obj.write(text)
file_obj.close()
