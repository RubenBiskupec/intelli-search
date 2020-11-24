import os
path = '/Users/rubenbiskupec/Desktop/intelli-search/documents'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, 'document'.join([str(index), '.pdf'])))