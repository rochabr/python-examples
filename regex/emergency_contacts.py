# Import the module
# Import the module
from docx import *

# Open the .docx file
document = Document('doc.docx')
document.save('new-file-name.docx')

# Search returns true if found

print(document.part)

i = 0

for paragraph in document.paragraphs:

    print(i)
    i += 1
    print(paragraph.text)

