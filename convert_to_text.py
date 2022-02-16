import pytesseract
import pandas as pd

#Using pytesseract-OCR, converted image to text
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\thejas.n\AppData\Local\Programs\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(r'E:\Projects\Document_Parser\img02.jpg')

#string to list conversion
def Convert(string):
    li = list(string.split('"'))
    return li

#list item   
str1 = text
list1 = (Convert(str1))

#list to dataframe to convert text to csv
df1 = pd.DataFrame(list1)
df1.to_csv('doc2_2.csv', index = False)

