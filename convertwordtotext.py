import os
import zipfile
import xml.etree.ElementTree as ET

path = 'syllabi/'
list_of_docs = os.listdir(path)
print(list_of_docs)
for i in list_of_docs:
    
    try:
        word_document = zipfile.ZipFile(path+i).read('word/document.xml')
        b = str(word_document).split('>')
        finalSent = []
        for a in b:
            if '</w:t' in a:
                a = a.replace('</w:t','')
                finalSent.append(a)
        with open(i+'.txt','w') as f:
            for child in finalSent:
                print(child)
                f.write(child+'\n')
            print(f)
    except:
        print("it didn't work")
    