import numpy as np
import matplotlib.pyplot as plt
fGHz=np.arange(2,11,0.1)
fcenter = fGHz[len(fGHz)/2]
dist = np.arange(1,9,0.1)
LFS = -32.44 -20*np.log10(fcenter)-20*np.log10(dist)
tEtt = np.load('tEtt.npy')
tEtp = np.load('tEtp.npy')
tEpt = np.load('tEpt.npy')
tEpp = np.load('tEpp.npy')
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax.plot(dist,10*np.log10(tEtt))
ax.plot(dist,10*np.log10(tEtp))
ax.plot(dist,10*np.log10(tEpt))
ax.plot(dist,10*np.log10(tEpp))
ax.plot(dist,LFS,'k--')
plt.xlabel('Tx Rx distance (meters)')
plt.ylabel('Attenuation (dB)')
plt.title('Attenuation w.r.t distance - $\\tilde{C}$ level no antenna')
plt.legend((u'$\\theta\\theta$',u'$\\theta\phi$',u'$\phi\\theta$',u'$\phi\phi$','Free Space'))
plt.tight_layout()
fig.savefig('FriisCtilde.png')
