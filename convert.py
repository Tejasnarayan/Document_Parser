from pdf2image import convert_from_path

#get the pdf and convert to image(jpeg/png)
image1 = convert_from_path(r'Document_2.1.pdf', poppler_path= r'C:\Users\thejas.n\poppler-0.68.0_x86\poppler-0.68.0\bin')

for img in image1:
    img.save('img01.jpg','JPEG')

#get the pdf and convert to image(jpeg/png)
image2 = convert_from_path(r'Document_2.2.pdf', poppler_path= r'C:\Users\thejas.n\poppler-0.68.0_x86\poppler-0.68.0\bin')

for img in image2:
    img.save('img02.jpg','JPEG')

