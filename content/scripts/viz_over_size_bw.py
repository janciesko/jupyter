import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbrn
import pandas as pd
from matplotlib.colors import LogNorm
import sys
import os 
sbrn.set_context('paper')

_fontsize = 13

filename=sys.argv[1]
title="stream-increment, v100, single node"

custom = {"axes.edgecolor": "black","grid.linestyle": "dashed", "grid.color": "gray"}
sbrn.set_style("whitegrid", rc = custom)
 
dataSet = pd.read_table(filename, skiprows = 0, header=0, delimiter=",")
print(dataSet.head())
 
ax = sbrn.lineplot(data=dataSet, x="size", y="bw",hue="type",palette="flare",legend="full")
 
ax.set_xscale("log")
#ax.set_yscale("log")
ax.set_xlabel('view size (MB)',fontsize=_fontsize);
ax.set_ylabel('GB/s',fontsize=_fontsize);

#ax.legend(fontsize=_fontsize)
ax.legend(title="Kokkos view type") #, loc='lower right')
ax.set_title(title,fontsize=_fontsize)
  
#plt.tight_layout()
#plt.show()
filename_short=os.path.basename(filename)
plt.savefig("./PNG/"+filename_short+"_bw.png", dpi=300)
plt.savefig("./SVG/"+filename_short+"_bw.svg", dpi=300)
