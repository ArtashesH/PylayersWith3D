t=mgrid[-pi:pi:100j]
    mlab.plot3d(cos(t),sin(3*t),cos(5*t),color=(0.23,0.6,1),colormap='Spectral')
    mlab.colorbar()
    mlab.show()