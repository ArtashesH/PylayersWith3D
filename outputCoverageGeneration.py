from pylayers.gis.layout import *
# Load the layout from its .ini file in $BASENAME/struc/ini
L = Layout('WHERE1.lay')
# Build all the graphs
L.build()
# Check graphs
L._visual_check()
plt.show()