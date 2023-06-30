#!/usr/bin/python3
# sum_duration.py - uses ffmpeg and the duration script to display the 
# duration in seconds of each sample, and a total number of seconds duration

import subprocess
import os
import glob

inpath="../../data/mp3/"
flist=glob.glob(inpath+"*.mp3")
flist.sort()
tot=0.0
for fname in flist:
    list_files=subprocess.run(["./duration",fname],stdout=subprocess.PIPE)
    fdur=str(list_files.stdout)
    fdur=float(fdur[2:7])
    print(fname[len(inpath):],':',fdur)
    tot+=fdur
print("Total ",tot)


