import PyPDF2
import pandas as pd
	
pdfFileObj = open('Document 1.2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
	
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
	
pdfFileObj.close()


