#!/usr/bin/python3

import os

os.system('fswatch -0 /Users/mustakimahmedhasan/Downloads | xargs -0 -n 1 -I {} python3 /Users/mustakimahmedhasan/Workspace/Programming/Python/file-management-system/script.py')
print('launcher running!')