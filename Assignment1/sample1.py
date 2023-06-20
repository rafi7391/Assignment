import re
import PyPDF2
# Open the PDF file
pdfFile = open('sample1.pdf', 'rb')
# Creating the pdfReader object
pdfReader = PyPDF2.PdfReader(pdfFile)
# Get the number of pages in the PDF
numPages = len(pdfReader.pages)
# Loop over the pages in the PDF
for i in range(numPages):
    # Get the page object
    page = pdfReader.pages[i]
    # Get the text from the page
    text = page.extract_text()
    # Find all the key-value pairs in the text
    keyValuePairs = re.findall(r'(?P<key>[^=]+)=(?P<value>.+)$', text)
    # Print the key-value pairs
    for key, value in keyValuePairs:
        print(f'{key}: {value}')
# Close the PDF file
pdfFile.close()
