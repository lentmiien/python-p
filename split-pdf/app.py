import os
from pathlib import Path
import PyPDF2

for filename in Path(Path.home(), 'Documents', 'sp', 'in').glob('*.pdf'):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(pdfReader.numPages):
        pdfWriter = PyPDF2.PdfFileWriter()
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        pdfOutputFile = open(
            Path(Path.home(), 'Documents', 'sp', 'out', filename.stem + str(pageNum) + '.pdf'), 'wb')
        pdfWriter.write(pdfOutputFile)
        pdfOutputFile.close()
    pdfFileObj.close()
