try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('/home/chinmay/Documents/Python/test_images/IMG-20160711-WA0002.jpg'))


'''import cv2
import pytesseract

img = cv2.imread('/home/chinmay/Documents/Python/test_images/IMG-20160925-WA0041.jpg')

h, w, c = img.shape

boxes = pytesseract.image_to_boxes(img) 


for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)'''