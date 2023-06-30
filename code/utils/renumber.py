# renumber.py - renumbers EmoGator samples so the participant ID is sequential

import os
import glob

inpath="../../data/mp3/"
os.chdir(inpath) # keeps the glob paths short
flist=glob.glob("*.mp3")
flist.sort()
outsid=1
lastsid=1
for fname in flist:
    insid=int(fname[0:6])
    if insid>lastsid:
        lastsid=insid
        outsid+=1
    newname="%06d%s" % (outsid,fname[6:])
    print(fname,'->',newname)
    if fname!=newname:
        os.rename(fname,newname)
print('last sid input:',lastsid,'last sid output:',outsid)
