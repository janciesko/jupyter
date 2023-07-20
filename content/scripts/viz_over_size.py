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
title="Stream-Update, kokkos-dev-2, single node"

custom = {"axes.edgecolor": "black","grid.linestyle": "dashed", "grid.color": "gray"}
sbrn.set_style("whitegrid", rc = custom)
 
dataSet = pd.read_table(filename, skiprows = 0, header=0, delimiter=",")
print(dataSet.head())
 
ax = sbrn.lineplot(data=dataSet, x="size", y="gups",hue="type",palette="flare",legend="full")
 
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel('data_size (MB)',fontsize=_fontsize);
ax.set_ylabel('GUPs',fontsize=_fontsize);

#ax.legend(fontsize=_fontsize)
ax.legend(title=title) #, loc='lower right')
ax.set_title(title,fontsize=_fontsize)
  
plt.tight_layout()
#plt.show()
filename_short=os.path.basename(filename)
plt.savefig("./PNG/"+filename_short+".png", dpi=300)
plt.savefig("./SVG/"+filename_short+".svg", dpi=300)
