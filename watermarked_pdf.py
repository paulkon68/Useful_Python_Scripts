# Watermarks a pdf, with a watermaked (one-paged) pdf
# You should provide both 

import PyPDF2

template = PyPDF2.PdfFileReader(open('<pdf_to_be_watermarked.pdf>', 'rb'))
watermark = PyPDF2.PdfFileReader(open('<watermarked.pdf>', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)


with open('new_watermarked.pdf', 'wb') as file:
    output.write(file)
