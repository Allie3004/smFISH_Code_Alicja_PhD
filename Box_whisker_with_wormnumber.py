import sys
print(sys.version)

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import seaborn as sns
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

cwd = os.getcwd()
print(cwd)
#input directory
cells10 = 'H0', 'H1', 'H2', 'V1', 'V2', 'V3', 'V4','V5a','V5p','V6', 'T'
cells17 = 'H0', 'H1', 'H2', 'V1', 'V2', 'V3', 'V4','V5','V6', 'T'
cells_d1 = 'H0', 'H1a','H1p', 'H2a','H2p', 'V1a','V1p', 'V2a','V2p', 'V3a', 'V3p','V4a','V4p','V5a','V5p','V6a','V6p', 'Ta', 'Tp'
cells_d2 = 'H0', 'H1a','H1p', 'H2a','H2p', 'V1aa','V1ap','V1pa','V1pp', 'V2aa','V2ap', 'V2pa','V2pp', 'V3aa', 'V3ap','V3pa', 'V3pp','V4aa','V4ap','V4pa','V4pp','V5aa','V5ap','V5pa','V5pp','V6aa','V6ap','V6pa','V6pp', 'Taa', 'Tap','Tpa', 'Tpp'
cwd = os.getcwd()
os.chdir("/Users/alicja/Desktop")
#print(cwd)
#Change the file name
probe = 'ceh-16'
hours = '10'
strain = 'ceh-16(bp323)'
file = pd.read_csv(r'pop-1_cehegl_jr.csv', header = 0)
Cell_ND = []
Cell_D = []
Cell_DD = []
"""
file1 = file[file['Time']==17]
file2 = file[file['Time']==10]
file = file[file['Time']==26]
"""
#Cell_ND = file[file['Seam_Cell'].isin(cells10)]

Cell_D = file[file['Seam_Cell'].isin(cells_d1)]
Cell_DD = file[file['Seam_Cell'].isin(cells_d2)]





#fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(15,10), sharey = True)
fig, ax1 = plt.subplots(1,1)
#bplot = sns.boxplot(y = 'mRNA', x = 'Seam_Cell', data = file2, order = cells10, whis = 2.5,color = "lightcoral", width = 0.3, ax = ax1)
#bplot = sns.boxplot(y = 'mRNA', x = 'Seam_Cell', data = file1, order = cells17, whis = 4,color = "lightgreen", width = 0.3, ax = ax2)
#bplot = sns.stripplot(y = 'mRNA', x = 'Seam_Cell', hue = 'Worm', data = Cell_ND, order = cells, jitter = True, marker = 'o', size = 4, palette = 'Spectral', ax = ax1)


bplot = sns.boxplot(y = 'mRNA', x = 'Seam_Cell', hue = 'Strain', data = Cell_D, order = cells_d1, whis = 2.5,palette = {"darkblue","skyblue"}, width = 0.6, ax = ax1)
#bplot = sns.stripplot(y = 'mRNA', x = 'Seam_Cell', hue = 'Worm', data = Cell_D, order = cells_d1, jitter = True, marker = 'o', size = 4, palette = 'Spectral', ax = ax2)
#bplot = sns.boxplot(y = 'mRNA', x = 'Seam_Cell', data = Cell_DD, order = cells_d2,whis = 2.5, palette = {"thistle","darkmagenta"}, width = 0.6, ax = ax4)
#bplot = sns.stripplot(y = 'mRNA', x = 'Seam_Cell', hue = 'Worm', data = Cell_DD, order = cells_d2, jitter = True, marker = 'o', size = 4, palette = 'Spectral', ax = ax3)
#Change the plot title
#ax2.get_legend().remove()
#ax3.get_legend().remove()
#ax1.get_legend().remove()
ax1.set_ylabel(str(probe)+' mRNA counts at early L1', fontsize = 11)
ax1.tick_params(axis="x", labelsize=10)
ax1.set_xlabel('Seam Cell', fontsize = 11)
"""
ax2.set_ylabel(str(probe)+' mRNA counts at late L1', fontsize = 11)
ax3.set_ylabel(str(probe)+' mRNA counts at early L2', fontsize = 11)
ax4.set_ylabel(str(probe)+' mRNA counts at late L2', fontsize = 11)
ax2.set_xlabel('Seam Cell', fontsize = 11)
ax3.set_xlabel('Seam Cell',fontsize = 11)
ax4.set_xlabel('Seam Cell',fontsize = 11)
ax3.tick_params(axis="x", labelsize=10)
ax2.tick_params(axis="x", labelsize=10)
"""
#fig.suptitle(str(probe)+' probe in '+str(strain)+' at '+str(hours)+' hours')
plt.subplots_adjust(left=0.1, bottom=0.05, right=0.9, top=0.95, hspace = 0.3)
plt.show()
