import PyPDF2

def extract_key_value_pairs(sample1):
    keyValuePairs = []  # Define the variable here
    
    with open(sample1, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Extract text from each page
        for page in reader.pages:
            text = page.extract_text()
            
            # Process the extracted text to find key-value pairs
            lines = text.split('\n')
            for line in lines:
                # Assuming the key-value pairs are separated by a colon (e.g., "Key: Value")
                if ':' in line:
                    key, value = line.split(':', 1)  # Split at the first occurrence of ':'
                    key = key.strip()  # Remove leading/trailing spaces from the key
                    value = value.strip()  # Remove leading/trailing spaces from the value
                    keyValuePairs.append([key, value])
    
    return keyValuePairs
