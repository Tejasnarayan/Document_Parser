from distutils.command.config import config
import sys,fitz
import spacy
from pdf2image import convert_from_path
import pytesseract
from spacy import displacy
import pandas as pd


fname = 'E:\Projects\Document_Parser\Phase_2\Document 1.1.pdf'
doc= fitz.open(fname)
doc1=""
for page in doc:
  doc1 = doc1 + str(page.getText())
print(doc1)

fname = 'E:\Projects\Document_Parser\Phase_2\Document 1.2.pdf'
doc= fitz.open(fname)
doc2=""
for page in doc:
  doc2 = doc2 + str(page.getText())
print(doc2)

fname = 'E:\Projects\Document_Parser\Phase_2\Document 3.1.pdf'
doc= fitz.open(fname)
doc3=""
for page in doc:
  doc3 = doc3 + str(page.getText())
print(doc3)


fname = 'E:\Projects\Document_Parser\Phase_2\Document 3.2.pdf'
doc= fitz.open(fname)
doc4=""
for page in doc:
  doc4 = doc4 + str(page.getText())
print(doc4)

fname = 'E:\Projects\Document_Parser\Phase_2\Document 4.1.pdf'
doc= fitz.open(fname)
doc5=""
for page in doc:
  doc5 = doc5 + str(page.getText())
print(doc5)

fname = 'E:\Projects\Document_Parser\Phase_2\Document 4.2.pdf'
doc= fitz.open(fname)
doc6=""
for page in doc:
  doc6 = doc6 + str(page.getText())
print(doc6)


## Conversion of Document_5.1 to an image.
image = convert_from_path(r'Document 5.1.pdf', poppler_path= r'C:\Users\thejas.n\poppler-0.68.0_x86\poppler-0.68.0\bin')
for img in image:
    img.save('image7.jpg','JPEG')

## Conversion of Document_5.2 to an image.
image = convert_from_path(r'Document 5.2.pdf', poppler_path= r'C:\Users\thejas.n\poppler-0.68.0_x86\poppler-0.68.0\bin')
for img in image:
    img.save('image8.jpg','JPEG')

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\thejas.n\AppData\Local\Programs\Tesseract-OCR\tesseract'
doc7 = pytesseract.image_to_string(r'E:\Projects\Document_Parser\Phase_2\image7.jpg')
doc8 = pytesseract.image_to_string(r'E:\Projects\Document_Parser\Phase_2\image8.jpg')


docs = doc1+doc2+doc3+doc4+doc5+doc6+doc7+doc8

text_file = open("E:\Projects\Document_Parser\Phase_2\Doc.txt", "w",encoding="utf-8") 
#write string to file
text_file.write(docs)
#close file
text_file.close()

from spacy.tokens import DocBin
from tqdm import tqdm
import spacy

nlp = spacy.blank("en")
db = DocBin()

import json
f = open("annotations_train.json",encoding = 'utf-8')
TRAIN_DATA = json.load(f)
print(TRAIN_DATA)


f = open("annotations_test.json")
VAL_DATA = json.load(f)
print(VAL_DATA)

#creating an spacy object for training data
for text, annot in tqdm (TRAIN_DATA['annotations']):
  doc = nlp.make_doc(text)
  ents = []
  for start, end, label in annot["entities"]:
    span =  doc.char_span(start, end, label = label,alignment_mode = "contract")
    if span is None:
      print("Skipping Entity")
    else:
      ents.append(span)
  doc.ents = ents
  db.add(doc)
db.to_disk("./training_data.spacy")

#creating an spacy object for testing/validation data
for text, annot in tqdm (VAL_DATA['annotations']):
  doc = nlp.make_doc(text)
  ents = []
  for start, end, label in annot["entities"]:
    span =  doc.char_span(start, end, label = label,alignment_mode = "contract")
    if span is None:
      print("Skipping Entity")
    else:
      ents.append(span)
  doc.ents = ents
  db.add(doc)
db.to_disk("./validation_data.spacy")

nlp_ner = spacy.load("E:\Projects\Document_Parser\Phase_2\model-best")
doc = nlp_ner("Summary page NAMED INSURED:  Violet McKenzie POLICY NUMBER:  X7V9IOLCNQW ADDRESS: LOCATION #1 \
- O Hare Cargo Area Rd, Chicago, Indiana, Code - 60666 Homeowners Insurance Policy Coverage Disclosure Summary\
 This form is promulgated pursuant to LSA - R.S. 22:1332. THIS   IS   ONLY   A   SUMMARY   OF   YOUR   COVERAGE   AND   DOES   NOTAMEND,  EXTEND   OR ALTER   \
THE   COVERAGES   OR   ANY   OTHER   PROVISIONS CONTAINED IN YOUR POLICY. INSURANCE IS A \
CONTRACT. THE LANGUAGE IN YOUR POLICY CONTROLS YOUR LEGAL RIGHTS AND OBLIGATIONS. \
READ YOUR INSURANCE POLICY FOR COMPLETEPOLICY TERMS AND CONDITIONS COVERAGE(S) \
FOR WHICH PREMIUM WAS PAID Deductibles : This policy sets forth certain deductibles that will be applied to  claims  for  damages. When applicable, a \
deductible will be subtracted from your total claim and you will be paid the balance, subject  to  \
applicable  coverage  limits. You   may   be   able   to   reduce   your   premium   by   increasing   your\
 deductible. Contact your producer (agent) or insurer for details. Other Structures Personal Property Loss  of Use Ordinance or Law \
 Personal Liability Medical Payments Water Backup & Sump Pump Overflow Limited Fungi, Wet/Dry Rot, or Bacteria\
     Loss Assessment Business PropertyHO3 Dwelling NOTICE: This policy does set forth a separate deductible for covered\
         losses caused by named storm as defined in the policy  number: X7V9IOLCNQW If the total insured value of the dwelling or Coverage A is $200,000.00 and  you  have  a  2%  hurricane,  \
wind  or  named  storm  deductible,  then  your hurricane, wind or named storm deductible would be \
$200,000.00 X .02 = $4,000.00.Losses: Coverage A - Dwelling $4,321.00 , Coverage B - $932.00, Coverage C - Personal Property $2226.00\
, Coverage D - Loss Of Use $9864.00 Summary page NAMED INSURED: POLICY NUMBER: ADDRESS: Simone Satterfield MZHAT41737H   \
5900 S Lake Dr, Cudahy, West Virginia, Code 53110 COVERAGE LIMIT DETAILS: COVERAGE A  - DWELLING (RCV) $1,036.00\
 COVERAGE B - $1,032.00 COVERAGE C - PERSONAL PROPERTY (RCV) $2134.00 COVERAGE D - LOSS OF USE $8346.00")


for ent in doc.ents:
  print (ent.text, ent.label_)