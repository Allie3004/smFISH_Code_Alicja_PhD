import sys
import pandas as pd
import numpy as np
import os
os.chdir("/Users/alicja/Desktop/egl-18_cy5_elt-1_red_in_ceh_mut")
file = pd.read_csv(r'egl-18_at_26hrs_ceh_mut.csv', header = 0)
hours_of_development = 26
worms = file['Worm'].values.ravel()
#worms = pd.unique(worms)
sets = 1
l2_cells = {'V1':['h','j','k','l'],'V2':['n','m','t','y'],'V3':['u','i','o','p'],'V4':['1','2','3','5'],'V5':['6','7','8','9'],'V6':['0','e','v','b'],'T':['+','.','<','-']}
#print(l2_cells['V1'][1])
#cells = 'V1','V2','V3','V4','V6'
cells = 'V1','V2'
worms = 1,6,87
for worm in worms:
    set = file[file['Worm']==worm]
    for cell in cells:
        """
    set['ROI_attribute'] = set['ROI_attribute'].replace({'a':'H0'})
    if 's' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'s':'H1a','d':'H1p'})
    elif 'd' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'d':'H1'})
    if 'f' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'f':'H2a','g':'H2p'})
    elif 'g' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'g':'H2'})

    for cell in cells:
        print(set['ROI_attribute'])
        #if l2_cells[str(cell)][0] and l2_cells[str(cell)][2] in set['ROI_attribute']:
            #set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][0]:str(cell)+'aa',l2_cells[str(cell)][1]:str(cell)+'ap',l2_cells[str(cell)][2]:str(cell)+'pa',l2_cells[str(cell)][3]:str(cell)+'pp'})
            print('d')
        elif (l2_cells[str(cell)][0] and l2_cells[str(cell)][3]) in set['ROI_attribute']:
            print('a')
            #set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][0]:str(cell)+'aa',l2_cells[str(cell)][1]:str(cell)+'ap',l2_cells[str(cell)][3]:str(cell)+'p'})
        elif (l2_cells[str(cell)][1] and l2_cells[str(cell)][2]) in set['ROI_attribute']:
            print('b')
            #set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][1]:str(cell)+'a',l2_cells[str(cell)][2]:str(cell)+'pa',l2_cells[str(cell)][3]:str(cell)+'pp'})
        elif ('j' and 'l') in set['ROI_attribute']:
            print('c')
            #set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][1]:str(cell)+'a',l2_cells[str(cell)][3]:str(cell)+'p'})
            """
        if (l2_cells[str(cell)][3]) in set['ROI_attribute']:
            #set['ROI_attribute'] = set['ROI_attribute'].replace({l2_cells[str(cell)][3]:str(cell)})
            print('bla')
    #print(set)
        """
    if 'h' and 'k' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'h':'V1aa','j':'V1ap','k':'V1pa','l':'V1pp'})
    elif 'h' and 'l' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'h':'V1aa','j':'V1ap','l':'V1p'})
    elif 'j' and 'k' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'j':'V1a','k':'V1pa','l':'V1pp'})
    elif 'j' and 'l' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'j':'V1a','l':'V1p'})
    elif 'l' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'l':'V1p'})
    if 'n' and 't' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'h':'V2aa','j':'V2ap','k':'V2pa','l':'V2pp'})
    elif 'm' and 't' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'j':'V2a','k':'V2pa','l':'V2pp'})
    elif 'n' and 'y' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'h':'V2aa','j':'V2ap','l':'V2p'})
    elif 'm' and 'y' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'j':'V2a','l':'V2p'})
    elif 'y' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'l':'V2p'})
    if 'u' and 'o' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'h':'V3aa','j':'V3ap','k':'V3pa','l':'V3pp'})
    elif 'i' and 'o' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'j':'V3a','k':'V3pa','l':'V3pp'})
    elif 'u' and 'p' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'h':'V3aa','j':'V3ap','l':'V3p'})
    elif 'i' and 'p' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'j':'V3a','l':'V3p'})
    elif 'p' in set['ROI_attribute'].unique():
        set['ROI_attribute'] = set['ROI_attribute'].replace({'l':'V2p'})
        """
#print(set)
