import os
import sys
from tesserocr import PyTessBaseAPI

## $ pip install tesserocr

srcFolder = '/Users/rubenbiskupec/Desktop/intelli-search/documents-prova/'
dstFolder = '/Users/rubenbiskupec/Desktop/intelli-search/documents3/'

# os.walk generates the file names in a directory tree 
# we only need the first iteration
for subdir, dirs, images in os.walk(srcFolder):
    break
    
print("working on dir ", subdir)
print("sub dirs ", dirs)
print("---------------------------------------")
original = sys.stdout
### for every folder in srcFolder
for folder in dirs:
    print("processing folder /",folder)
    print("********************************")
    ### create a new filepath
    newFolder = srcFolder + folder + '/'
    newTxtFile = dstFolder + folder + '.txt'
    # create and open file, "a" is for append so that 
    # it doesn't get overwritten
    with open(newTxtFile, "a") as txtFile:
        ### get a list of images in this folder
        for subdir2, dirs2, images2 in os.walk(newFolder):
            print("images ", images2)
            ### for each image in the folder
            i = 0
            for image in images2:
                if (image != ".DS_Store"):
                    imagePath = newFolder + str(i) + 'image.png'
                    print("processing ", i,'image.png')
                    with PyTessBaseAPI() as api:
                        api.SetImageFile(imagePath)
                        txtFile.write(api.GetUTF8Text())
                        print("converted ", i, 'image.png', " to txt")
                    i = i+1
            break
    ## txtFIle gets automatically closed 
print("=======================")
print("converted every file :)")
print("time for pre processing")
print("AUTHOR:  Ruben Biskupec")
print("=======================")
