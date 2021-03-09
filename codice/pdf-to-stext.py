# This option did not work well enough to us, that is why we used proceded with
# pdf -> png -> txt

import pdftotext
import os
import sys 

original_stdout = sys.stdout # Save a reference to the original standard output

srcDir = '/Users/rubenbiskupec/Desktop/intelli-search/documents1/'
dstDir = '/Users/rubenbiskupec/Desktop/intelli-search/documents2/'
documents = os.listdir(srcDir)

for index, document in enumerate(documents):
    srcName = str(index) + 'document.pdf'
    dstName = str(index) + 'document.txt'
    document1 = srcDir + srcName
    document2 = dstDir + dstName
    
    try:
        with open(document1, "rb") as srcFile:
            try:
                pdf = pdftotext.PDF(srcFile)
            except IOError:
                print("document ", index, "not accessible")
            with open(document2, 'w') as dstFile:
                ## Change the standard output to the file we created.
                sys.stdout = dstFile
                for page in pdf:
                    print(page)
    except IOError:
        print("document ", index, "not accessible")
        
    srcFile.close()
    dstFile.close()

    sys.stdout = original_stdout
    print("converted document ", index)

sys.stdout = original_stdout # Reset the standard output to its original value
