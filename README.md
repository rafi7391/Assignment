# DeepLogic AI Assignment

## Assignment-1 Details

Created a Python Script that can extract Key-Value pairs from the given PDF.

This script will extract all the key-value pairs from the PDF file and print them to the console. The key-value pairs will be in the format `key: value`.
The `PyPDF2` library is used to read the PDF file. The `PdfFileReader` object is used to get the number of pages in the PDF and to get the text from each page. The `re` module is used to find all the key-value pairs in the text.

A CSV file that contains the extracted data.

The file 'sample1.csv' that contains the extracted data.The CSV file will have two columns: 'key' and 'Value'. 


## Assignment-2 Details

The 'index.html' file can create the sample flask webpage that allows users to upload a PDF file, and displays the extracted  data on the web page.

Here, I have created the flask application and defines two routes:'/' and '/extract'. The '/' route renders the 'index.html' page, which contains the form for uploading the PDF file. The `/extract` route handles the form submission and extracts the data from the PDF file. The extracted data is then rendered to the results.html page.

