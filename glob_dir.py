import glob  
  
# Using '*' pattern  
print('\nNumber of files') 
files = glob.glob('/media/chinmay/TOSHIBA EXT/P_bckp_8_2020/WhatsApp/Media/WhatsApp Images/*.jpg') 

a = len(files)
print(a)

'''for name in files:
    print(name) '''
