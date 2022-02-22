import sys
import pandas as pd
import numpy as np
import os
os.chdir("/Users/alicja/Desktop/egl-18_cy5_elt-1_red_in_ceh_mut")
file = pd.read_csv(r'egl-18_at_26hrs_ceh_mut.csv', header = 0)
strain= 'ceh-16_bp323_'
probe = 'egl-18_cy5'
hours_of_development = 26
worms = file['Worm'].values.ravel()
worms = pd.unique(worms)
sets = 1
l2_cells = {'V1':['h','j','k','l'],'V2':['n','m','t','y'],'V3':['u','i','o','p'],'V4':['1','2','3','5'],'V5':['6','7','8','9'],'V6':['0','e','v','b'],'T':['+','.','<','-']}
#print(l2_cells['V1'][1])
cells = 'V1','V2','V3','V4','V6','T'
#cells = 'V1','V2','V3'
#worms = 1,6,87
sets = 'a'
for worm in worms:

    set = file[file['Worm']==worm]
    set['ROI_attribute'] = set['ROI_attribute'].replace({'a':'H0'})
    if 's' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'s':'H1a','d':'H1p'})
    elif 'd' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'d':'H1'})
    if 'f' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'f':'H2a','g':'H2p'})
    elif 'g' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'g':'H2'})
    if l2_cells['V5'][3] in set['ROI_attribute'].unique():
        if l2_cells['V5'][1] in set['ROI_attribute'].unique():
            if l2_cells['V5'][0] in set['ROI_attribute'].unique():
                if l2_cells['V5'][2] in set['ROI_attribute'].unique():
                    set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells['V5'][0]:'V5aa',l2_cells['V5'][1]:'V5ap',l2_cells['V5'][2]:'V5pa',l2_cells['V5'][3]:'V5pp'})
                else:
                    set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells['V5'][0]:'V5aa',l2_cells['V5'][1]:'V5ap',l2_cells['V5'][3]:'V5p'})
            elif l2_cells['V5'][2] in set['ROI_attribute'].unique():
                set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells['V5'][1]:'V5a',l2_cells['V5'][2]:'V5pa',l2_cells['V5'][3]:'V5pp'})
            else:
                set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells['V5'][1]:'V5a',l2_cells['V5'][3]:'V5p'})
        elif l2_cells['V4'][3] in set['ROI_attribute'].unique():
            if l2_cells['V4'][1] in set['ROI_attribute'].unique():
                set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells['V5'][3]:'V5pp'})
        elif l2_cells['V6'][3] in set['ROI_attribute'].unique():
            if l2_cells['V6'][1] in set['ROI_attribute'].unique():
                set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells['V5'][3]:'V5pp'})
        else:
            set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells['V5'][3]:'V5'})

    for cell in cells:
        if (l2_cells[str(cell)][0] in set['ROI_attribute'].unique() and l2_cells[str(cell)][2]) in set['ROI_attribute'].unique():
            set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][0]:str(cell)+'aa',l2_cells[str(cell)][1]:str(cell)+'ap',l2_cells[str(cell)][2]:str(cell)+'pa',l2_cells[str(cell)][3]:str(cell)+'pp'})
        elif (l2_cells[str(cell)][0] in set['ROI_attribute'].unique() and l2_cells[str(cell)][3]) in set['ROI_attribute'].unique():
            set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][0]:str(cell)+'aa',l2_cells[str(cell)][1]:str(cell)+'ap',l2_cells[str(cell)][3]:str(cell)+'p'})
        elif (l2_cells[str(cell)][1] in set['ROI_attribute'].unique() and l2_cells[str(cell)][2]) in set['ROI_attribute'].unique():
            set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][1]:str(cell)+'a',l2_cells[str(cell)][2]:str(cell)+'pa',l2_cells[str(cell)][3]:str(cell)+'pp'})
        elif l2_cells[str(cell)][1] in set['ROI_attribute'].unique() and l2_cells[str(cell)][3] in set['ROI_attribute'].unique():
            set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][1]:str(cell)+'a',l2_cells[str(cell)][3]:str(cell)+'p'})
        elif l2_cells[str(cell)][3] in set['ROI_attribute'].unique():
            set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][3]:str(cell)})
    """
    if sets == 'a':
        sets = set
    else:
        print('b')
    """
    file.update(set)
file.columns = ['Cell','Worm','mRNA']
print(file)
file.to_csv(str(probe)+'_at_'+str(hours_of_development)+'_in_'+str(strain)+'.csv', index = False, header = True)
