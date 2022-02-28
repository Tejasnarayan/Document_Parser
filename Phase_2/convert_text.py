import sys,fitz
import spacy

fname = 'E:\projects\Document_Parsing2\Sample\Document_1.1.pdf'
doc= fitz.open(fname)
doc1=""
for page in doc:
  doc1 = doc1 + str(page.getText())
print(doc1)

fname = 'E:\projects\Document_Parsing2\Sample\Document_1.2.pdf'
doc= fitz.open(fname)
doc2=""
for page in doc:
  doc2 = doc2 + str(page.getText())
print(doc2)

fname = 'E:\projects\Document_Parsing2\Sample\Document_3.1.pdf'
doc= fitz.open(fname)
doc3=""
for page in doc:
  doc3 = doc3 + str(page.getText())
print(doc3)


fname = 'E:\projects\Document_Parsing2\Sample\Document_3.2.pdf'
doc= fitz.open(fname)
doc4=""
for page in doc:
  doc4 = doc4 + str(page.getText())
print(doc4)

fname = 'E:\projects\Document_Parsing2\Sample\Document_4.1.pdf'
doc= fitz.open(fname)
doc5=""
for page in doc:
  doc5 = doc5 + str(page.getText())
print(doc5)

fname = 'E:\projects\Document_Parsing2\Sample\Document_4.2.pdf'
doc= fitz.open(fname)
doc6=""
for page in doc:
  doc6 = doc6 + str(page.getText())
print(doc6)


fname = 'E:\projects\Document_Parsing2\Sample\Document_5.1.pdf'
doc= fitz.open(fname)
doc7=""
for page in doc:
  doc6 = doc7 + str(page.getText())
print(doc7)


fname = 'E:\projects\Document_Parsing2\Sample\Document_5.2.pdf'
doc= fitz.open(fname)
doc8=""
for page in doc:
  doc8 = doc8 + str(page.getText())
print(doc8)



test = spacy.load("en_core_web_sm")
ts = test(" ".join(doc1.split('\n')))
#print(ts)
for ent in ts.ents:
  if ent.label_.upper() == 'PERSON':
    print(f'{ent.label_.upper():{10}} - {ent.text}')