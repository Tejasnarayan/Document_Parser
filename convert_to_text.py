import pytesseract
import pandas as pd
import re

#Using pytesseract-OCR, converted image to text
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\thejas.n\AppData\Local\Programs\Tesseract-OCR\tesseract'
string1 = pytesseract.image_to_string(r'E:\Projects\Document_Parser\img01.jpg')
string2 = pytesseract.image_to_string(r'E:\Projects\Document_Parser\img02.jpg')

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



  df=pd.DataFrame([{'Name':name,
                 'Policy Number':policy,
                 'Street':address_street,
                 'City/Town': address_city,
                  'State/Province/Region':address_state,
                  'Zip/Postal Code':city_code,
                  'Coverage_A':coverage_a,
                  'Coverage_B':coverage_b,
                  'Coverage_C':coverage_c,
                  'Coverage_D':coverage_d}])
  df=df.append(df)
  return df

df1 = info(df,string1)

def details_df(string):
  temp=string.split('\n')
  temp=list(filter(lambda x: x!='',temp))
  name=temp[1].split(':')[1]
  policy=temp[2].split(':')[1]
  address_street=temp[4]
  address_city=temp[5]
  address_state=temp[6]
  city_code= re.findall('[0-9]+',temp[7])[0]
  coverage_a=temp[9].split('-')[1]
  coverage_b=temp[10].split('-')[1]
  coverage_c=temp[11].split('-')[1]
  coverage_d=temp[12].split('-')[1]

  df=pd.DataFrame([{'Name':name,
                 'Policy Number':policy,
                 'Street':address_street,
                 'City/Town': address_city,
                  'State/Province/Region':address_state,
                  'Zip/Postal Code':city_code,
                  'Coverage_A':coverage_a,
                  'Coverage_B':coverage_b,
                  'Coverage_C':coverage_c,
                  'Coverage_D':coverage_d}])

  return df
df=pd.DataFrame()  
for str in [string1,string2]:
    df=df.append(details_df(str))
df.reset_index(inplace=True) 
document = ["Document 1", "Document 2"]
print(document)
df.insert(1,"Document",document)
df.drop('index',axis=1,inplace=True)
print(df)
df.to_csv('result.csv')


