import glob  
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import shutil
import os.path 

#Path Initialization
#################################
base_dir = '<path to folder with mixed images>/*.jpg'
no_text_dir = '<path to folder where images with no text needs to be copied>'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename)) 
    return text

def check_if_all_none(list_of_elem):
    for elem in list_of_elem:
        if (ord(elem) != 10 and ord(elem) != 32 and ord(elem) != 12): 
            return True
    return False

print('\nNumber of files : ') 
files = glob.glob(base_dir) 
a = len(files)
print(a)

for count,name in enumerate(files):
	print ("**  "+ str(count+1)+" :  "+name+"  **")
	words = ocr_core(name)
	res = check_if_all_none(words)
	if(res == False):
		basename = os.path.basename(name) 
		shutil.move(name, no_text_dir+str(basename))
		print("Moved")
