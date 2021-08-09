from pylayers.antprop.antenna import *
import pylayers.util.mayautil as myu
A = Antenna('S1R1.vsh3')

lvsh3 = A.ls('vsh3')
lssh3 = A.ls('sh3')
lmat = A.ls('mat')
print("Number of antenna in .vsh3 format : ",len(lvsh3))
print("Number of antenna in .sh3 format : ",len(lssh3))
print(lvsh3[0:5])
print(lssh3[0:5])
print(lmat[0:5])

A.eval(grid=True)

f = plt.figure(figsize=(20,10))
a1 = f.add_subplot(121,projection='polar')
f1,a1 = A.plotG(fGHz=[3,4,5.6],plan='theta',angdeg=0,GmaxdB=5,fig=f,ax=a1,show=False)
a2 = f1.add_subplot(122,projection='polar')
f2,a2 = A.plotG(fGHz=[3,4,5.6],plan='phi',angdeg=90,GmaxdB=5,fig=f,ax=a2)
f2.tight_layout()