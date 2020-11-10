"""
this script recieves 2 arguments: 
    FILE the file to be changed,
    ATTRIBUTION_COMMAND the line to replace the line that has the ATTRIBUTION_COMMAND left side as prefix    

you can use this to add attribution or change existing ones
"""

import sys

FILE = sys.argv[1]
ATTRIBUTION_COMMAND = sys.argv[2]
LEFT_SIDE = ATTRIBUTION_COMMAND.split('=')[0]

file_obj = open(FILE, 'r')
lines = file_obj.read().split('\n')
file_obj.close()

#find attribution and replace it
found = False
for i in range(len(lines)):
    if lines[i].startswith(LEFT_SIDE):
        lines[i] = ATTRIBUTION_COMMAND
        found = True
        break

if not found:
    lines.append(ATTRIBUTION_COMMAND)

#rewrite file
text = '\n'.join(lines)
file_obj = open(FILE, 'w')
file_obj.write(text)
file_obj.close()