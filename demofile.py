# -*- coding: utf-8 -*-
import os.path
a = os.path.abspath('demofile.py')
#a = os.path.abspath('.')
print(os.path.basename(a))
print(os.path.dirname(a))
print(os.path.split(a))
print(os.path.splitdrive(a))

import glob
files = glob.glob('demo/')
for f in files:
    print (f)
