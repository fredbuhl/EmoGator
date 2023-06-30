#!/usr/bin/python3

import os
import glob

inpath="../../data/mp3"
os.chdir(inpath) # keeps the glob paths short
flist=glob.glob('*.mp3')
flist.sort()
ulist={}
for file in flist:
    uid=file[:6]
    if uid in ulist.keys():
        ulist[uid]+=1
    else:
        ulist[uid]=1
for uid in ulist.keys():
    print(uid,':',ulist[uid])

