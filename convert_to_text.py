import pytesseract
import pandas as pd

#Using pytesseract-OCR, converted image to text
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\thejas.n\AppData\Local\Programs\Tesseract-OCR\tesseract'
string1 = pytesseract.image_to_string(r'E:\Projects\Document_Parser\img01.jpg')

#coversion of doc2_1 to csv
df=pd.DataFrame()
def info(df,string):
  temp=string.split('\n')
  temp=list(filter(lambda x: x!='',temp))
  name=temp[1].split(':')[1]
  policy=temp[2].split(':')[1]
  address_street=temp[4]
  address_city=temp[5]
  address_state=temp[6]
  city_code=temp[7].split(':')[1]
  coverage_a=temp[9].split('-')[-1]
  coverage_b=temp[10].split('-')[-1]
  coverage_c=temp[11].split('-')[-1]
  coverage_d=temp[12].split('-')[-1]



  df1=pd.DataFrame([{'Name':name,
                 'Policy':policy,
                 'Address_Street':address_street,
                  'Address_City': address_city,
                  'Address_State':address_state,
                  'Address_City_Code':city_code,
                  'Coverage_A':coverage_a,
                  'Coverage_B':coverage_b,
                  'Coverage_C':coverage_c,
                  'Coverage_D':coverage_d}])
  df=df.append(df1)
  return df

df1 = info(df,string1)
df1.to_csv('doc2_1.csv')


