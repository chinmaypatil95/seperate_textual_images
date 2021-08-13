# Textual images seperator

Often time I have struggled to seperate unnecessary images which have text for eg. Memes from the actual personal images from the backup of photos that I have from old phone's whatsapp / telegram folder. This program is simply meant to seperate out textual and non textual images from specified folder. This do not guarantee that all of the seperated images would be correct, but it reduces manual task of finding out the personal images to a vast expense.

It uses pytesseract as OCR tool to recognize text in images, and if no text found moves that image to seperate folder.<br/> 
**base_dir** and **no_text_dir** needs to be changed to appropriate folder paths.
