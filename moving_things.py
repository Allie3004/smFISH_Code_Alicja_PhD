import os
import shutil
print(os.getcwd())

os.chdir('/Users/alicja/Desktop/egl-18_cy5_elt-1_red_in_ceh_mut/tiffs/analyzed')

for filename in os.listdir():
    if '45' in str(filename):
    #if '90' in str(filename):
        shutil.move(filename,'/Users/alicja/Desktop/egl-18_cy5_elt-1_red_in_ceh_mut/bin')

"""
for x in range(18,42):
    print(x)
    print('a'+str(x-1))
    os.rename('GFP0'+str(x)+'.tif', 'GFP0'+str(x-1)+'.tif')
"""
