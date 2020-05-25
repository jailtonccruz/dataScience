# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 02:25:48 2020

@author: jailton
"""
####################################
## Mineracao de textos
####################################
import matplotlib.pyplot as plt
import nltk
#nltk.download()
from nltk.corpus import PlaintextCorpusReader
# from nltk.corpus import 
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
import string

# Import all libraries
import PyPDF2 
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import 
from PyPDF2 import PdfFileReader, PdfFileWriter

## Step 2: Read PDF file

reader=PdfFileReader(open("C:\dataScience\MaterialApoio\PackageStratification",'rb'))

#Write a for-loop to open many files (leave a comment if you'd like to learn how).

filename = 'C:\dataScience\MaterialApoio\PackageStratification' 
filename
#open allows you to read the file.
pdfFileObj = open(filename,'rb')

#The pdfReader variable is a readable object that will be parsed.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Discerning thf pages will ae number ollow us to parse through all the pages.
num_pages = pdfReader.numPages
count = 0
text = ""

#The while loop will read each page.
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

#This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text

#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text.
else:
   text = textract.process(fileurl, method='tesseract', language='eng')

#Now we have a text variable that contains all the text derived from our PDF file. Type print(text) to see what it contains. It likely contains a lot of spaces, possibly junk such as '\n,' etc.
#Now, we will clean our text variable and return it as a list of keywords.