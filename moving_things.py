import os
import shutil
print(os.getcwd())

os.chdir('/Users/alicja/Desktop/pop-1_cy5_in_JR667/tiffs/analyzed')

for filename in os.listdir():
    if '30' in str(filename):
    #if '90' in str(filename):
        shutil.move(filename,'/Users/alicja/Desktop/pop-1_cy5_in_JR667/tiffs/trash')

"""
for x in range(18,42):
    print(x)
    print('a'+str(x-1))
    os.rename('GFP0'+str(x)+'.tif', 'GFP0'+str(x-1)+'.tif')
"""
