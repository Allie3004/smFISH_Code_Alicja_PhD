
import os

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
import scipy
from statannot import add_stat_annotation

os.chdir('/Users/alicja/Desktop/PhD_Year_1/old_data_17hrs')
cwd = os.getcwd()
print(cwd)

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
#matplotlib.rc('text', usetex = True)
cells = 'H0', 'H1', 'H2', 'V1', 'V2', 'V3', 'V4','V5','V6', 'T'
cells_ante = 'H1a', 'H2a', 'V1a', 'V1aa', 'V2a', 'V2aa', 'V3a', 'V3aa', 'V4a', 'V4aa', 'V5a', 'V5aa', 'V6a', 'V6aa', 'Ta', 'Taa'
cells_poste = 'H1p', 'H2p', 'V1p', 'V1pp', 'V2p', 'V2pp', 'V3p', 'V3pp', 'V4p', 'V4pp', 'V5p', 'V5pp', 'V6p', 'V6pp', 'Tp', 'Tpp'
#Enter filename

#all = pd.read_csv(r'Ceh-16_probe_all.csv', header = 0)
all1 = pd.read_csv(r'Ceh-16_probe_all.csv', header = 0)
#all2 = pd.read_csv(r'Egl-18_mRNA_JR667.csv', header = 0)
#all1 = all1[all1['Strain']!='ku491']
#mut = all[all['Strain'] == 'triple-hox']

cells_d1 = 'H0', 'H1a','H1p', 'H2a','H2p', 'V1a','V1p', 'V2a','V2p', 'V3a', 'V3p','V4a','V4p','V5a','V5p','V6a','V6p', 'Ta', 'Tp'
cells_d2 = 'H0', 'H1a','H1p', 'H2a','H2p', 'V1aa','V1ap','V1pa','V1pp', 'V2aa','V2ap', 'V2pa','V2pp', 'V3aa', 'V3ap','V3pa', 'V3pp','V4aa','V4ap','V4pa','V4pp','V5aa','V5ap','V5pa','V5pp','V6aa','V6ap','V6pa','V6pp', 'Taa', 'Tap','Tpa', 'Tpp'

#fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(16,6), sharey = True)
fig, ax1 = plt.subplots(1,1)
sns.boxplot(y = 'mRNA', x = 'Seam_cell', hue = 'Strain', order = cells, data = all, palette = 'Blues', width = 0.5, showfliers=True, ax = ax1)
ax1, test_results = add_stat_annotation(ax1, data=all, y = 'mRNA', x = 'Seam_cell',hue = 'Strain', order = cells, box_pairs=[(('WT(JR667),str(cell),"" "egl-18(ga97)"), ("WT(JR667)", "elt-1(ku491)") test='Mann-Whitney', text_format='star', loc='outside', verbose=2)
#sns.boxplot('mRNA', x = 'Seam_cell', hue = 'Strain', order = cells, data = all, palette = 'Greens', width = 0.5, showfliers=False, ax = ax2)
#sns.boxplot(y = 'mRNA', x = 'Seam_cell', hue = 'Strain', order = cells, data = all2, palette = 'Reds', width = 0.5, showfliers=True, ax = ax3)
#ax1.set_ylabel(r'$\mathit{ceh-16 }$ mRNA counts', fontsize = 12)
ax2.set_ylabel(r'$\mathit{egl-18 }$ mRNA counts',fontsize = 12)
#ax3.set_ylabel(r'$\mathit{egl-18 }$ mRNA counts',fontsize = 12)
#ax1.set_xlabel('Seam Cell')
ax2.set_xlabel('Time Point')
#ax3.set_xlabel('Seam Cell')
#ax1.legend(title = 'Strain', prop={'size': 10, 'style': 'italic'},loc = 'lower center', bbox_to_anchor = (0.5,-0.2), ncol = 3)
#ax2.legend(title = 'Strain', prop={'size': 10, 'style': 'italic'},loc = 'lower center', bbox_to_anchor = (0.5,-0.25), ncol = 4)
#ax3.legend(title = 'Strain', prop={'size': 10, 'style': 'italic'},loc = 'lower center', bbox_to_anchor = (0.5,-0.2), ncol = 3)
#ax2.set_ylim([0, all['mRNA'].max()*1.1])

#bplot = sns.boxplot(data = (mut, wild), x = 'Cell', y = 'mRNA', showcaps=False, boxprops = {'facecolor':'None', 'zorder':10}, showfliers=False ,showmeans = True, meanprops={"marker":"s", "markerfacecolor":"white",  "markeredgecolor":"black","markersize":"3"},whiskerprops={'linewidth':0, "zorder":10}, ax = ax2, width = 0.5)
#bplot = sns.stripplot(y = 'mRNA', x = 'Cell', hue = 'Worm', data = (probe_ceh, probe_elt), jitter = True, marker = 'o', size = 4, palette = 'Spectral')

#plt.ylabel('ceh-16 cy5 mRNA levels in triple hox mutants')
#plt.legend(bbox_to_anchor = (1, 0.75), fontsize = 10, title = 'Probe')
"""
pvalues_ceh_in_egl = []
pvalues_ceh_in_elt = []
pvalues_elt_in_egl = []
pvalues_elt_in_ceh = []
pvalues_elt_in_cehegl = []
pvalues_egl_in_elt = []
pvalues_egl_in_ceh = []
pvalues_ceh_in_egl_star = list()
pvalues_ceh_in_elt_star = list()
pvalues_elt_in_egl_star = list()
pvalues_elt_in_ceh_star = list()
pvalues_elt_in_cehegl_star = list()
pvalues_egl_in_elt_star = list()
pvalues_egl_in_ceh_star = list()
def convert_pvalue_to_asterisks(pvalue):
    if pvalue <= 0.0001:
        return "****"
    elif pvalue <= 0.001:
        return "***"
    elif pvalue <= 0.01:
        return "**"
    elif pvalue <= 0.05:
        return "*"
    return "ns"

for cell in cells:

    a = all[all['Seam_cell']==cell]
    a1 = a[a['Strain']=='WT(JR667)']
    a2 = a[a['Strain']=='egl-18(ga97)']
    a3 = a[a['Strain']=='elt-1(ku491)']
    stats1, pvalue_ceh_in_egl = scipy.stats.mannwhitneyu((a1['mRNA']), (a2['mRNA']))
    pvalues_ceh_in_egl.append(pvalue_ceh_in_egl)
    stats2, pvalue_ceh_in_elt = scipy.stats.mannwhitneyu((a1['mRNA']), (a3['mRNA']))
    pvalues_ceh_in_elt.append(pvalue_ceh_in_elt)


    b = all1[all1['Seam_cell']==cell]
    b1 = b[b['Strain']=='WT(JR667)']
    b2 = b[b['Strain']=='egl-18(ga97)']
    b3 = b[b['Strain']=='ceh-16(bp323)']
    b4 = b[b['Strain']=='ceh-16(bp323);egl-18(ga97) ']
    stats3, pvalue_elt_in_egl = scipy.stats.mannwhitneyu((b1['mRNA']), (b2['mRNA']))
    pvalues_elt_in_egl.append(pvalue_elt_in_egl)
    stats4, pvalue_elt_in_ceh = scipy.stats.mannwhitneyu((b1['mRNA']), (b3['mRNA']))
    pvalues_elt_in_ceh.append(pvalue_elt_in_ceh)
    stats5, pvalue_elt_in_cehegl = scipy.stats.mannwhitneyu((b1['mRNA']), (b4['mRNA']))
    pvalues_elt_in_ceh.append(pvalue_elt_in_cehegl)

    c = all2[all2['Seam_cell']==cell]
    c1 = c[c['Strain']=='WT(JR667)']
    c2 = c[c['Strain']=='elt-1(ku491)']
    c3 = c[c['Strain']=='ceh-16(bp323)']
    stats5, pvalue_egl_in_elt = scipy.stats.mannwhitneyu((c1['mRNA']), (c2['mRNA']))
    pvalues_egl_in_elt.append(pvalue_egl_in_elt)
    stats6, pvalue_egl_in_ceh = scipy.stats.mannwhitneyu((c1['mRNA']), (c3['mRNA']))
    pvalues_egl_in_ceh.append(pvalue_egl_in_ceh)



for pvalues in pvalues_ceh_in_egl:
    pvalues_ceh_in_egl_star.append(convert_pvalue_to_asterisks(pvalues))
for pvalues in pvalues_ceh_in_elt:
    pvalues_ceh_in_elt_star.append(convert_pvalue_to_asterisks(pvalues))

for pvalues in pvalues_elt_in_egl:
    pvalues_elt_in_egl_star.append(convert_pvalue_to_asterisks(pvalues))
for pvalues in pvalues_elt_in_ceh:
    pvalues_elt_in_ceh_star.append(convert_pvalue_to_asterisks(pvalues))

for pvalues in pvalues_egl_in_elt:
    pvalues_egl_in_elt_star.append(convert_pvalue_to_asterisks(pvalues))
for pvalues in pvalues_egl_in_ceh:
    pvalues_egl_in_ceh_star.append(convert_pvalue_to_asterisks(pvalues))

y_position1 = all['mRNA'].max()*1.04
y_position2 = all['mRNA'].max()*1.01
for i in range (0,10):
    #ax1.text(i,y_position1, str(pvalues_ceh_in_egl_star[i]), horizontalalignment = 'center', fontsize = 11, fontweight = 'bold', fontstretch = 'extra-condensed',color = '#8ab9d3')
    #ax1.text(i,y_position2, str(pvalues_ceh_in_elt_star[i]), horizontalalignment = 'center', fontsize = 11, fontweight = 'bold', fontstretch = 'extra-condensed',color = '#3f83b1')
    ax2.text(i,y_position1, str(pvalues_elt_in_egl_star[i]), horizontalalignment = 'center', fontsize = 11, fontweight = 'bold', fontstretch = 'extra-condensed',color = '#398c5b')
    ax2.text(i,y_position2, str(pvalues_elt_in_ceh_star[i]), horizontalalignment = 'center', fontsize = 11, fontweight = 'bold', fontstretch = 'extra-condensed',color = '#8ec492')

    #ax3.text(i,y_position1, str(pvalues_egl_in_elt_star[i]), horizontalalignment = 'center', fontsize = 11, fontweight = 'bold', fontstretch = 'extra-condensed',color = '#c34341')
    #ax3.text(i,y_position2, str(pvalues_egl_in_ceh_star[i]), horizontalalignment = 'center', fontsize = 11, fontweight = 'bold', fontstretch = 'extra-condensed',color = '#ec8c72')

y_position = all['mRNA'].max() * 1.2
for idx, pval in enumerate(pvalue_asterisks):
    plt.text(x=idx, y=y_position, s=pval)
"""
plt.subplots_adjust(left=0.1, bottom=0.2, right=0.9, top=0.98, wspace = 0.1)
plt.show()
print(pvalues_ceh_in_egl_star)
