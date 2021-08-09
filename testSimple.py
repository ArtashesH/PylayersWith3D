from pylayers.antprop.coverage import *
from matplotlib.pyplot import * 
import time
import pdb
C = Coverage('E:/upworkProjs/FloorPlanAnalyzing/pylayers-master/data/ini/coverage.ini')
C.cover()
fig=plt.figure(figsize=(10,5))
C.L.display['nodes']=False
C.L.display['ednodes']=False
f,a = C.show(fig=fig)
f.savefig('result.png')
