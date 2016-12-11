# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
import isbnlib
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
#import shutil
#import glob

#os.chdir("C://Users//aozgursuz//Downloads") #os.chdir("\\media\\WD4TB\\")
#
#bas_dizin = os.getcwd()
#
##isimler = os.listdir(bas_dizin)
#
##print (isimler)
#
#dizin_isimleri = [name for name in os.listdir(bas_dizin) if os.path.isdir(os.path.join(bas_dizin, name))]
#print (dizin_isimleri)
#                  
#dosya_isimleri = [name for name in os.listdir(bas_dizin) if os.path.isfile(os.path.join(bas_dizin, name))]
#print (dosya_isimleri)
#
#for dosya in dosya_isimleri:
#    if dosya.endswith(".pdf"):
##        shutil.move(dosya, "C://Users//aozgursuz//Downloads//deneme")#os.chdir("\\media\\WD4TB\\PDF")

#her bir kitabın başlığının ilk harfiyle başlayan dizine taşı. Baş harf ile
#başlayan dizin yoksa dizini oluştur. Dosya adı mevcut mu? Kontrol et. Mevcut
#sa "chift" adında dizin oluştur ve içine taşı. "chift" içinde dosya adı mevcut
#mu? Kontrol et. Mevcut sa "chift" adında dizin oluştur ve içine taşı...
        
#==============================================================================
# A typical way to parse a PDF file is the following: 
# 
# from pdfminer.pdfparser import PDFParser, PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice
# 
# # Open a PDF file.
# fp = open('mypdf.pdf', 'rb')
# # Create a PDF parser object associated with the file object.
# parser = PDFParser(fp)
# # Create a PDF document object that stores the document structure.
# doc = PDFDocument()
# # Connect the parser and document objects.
# parser.set_document(doc)
# doc.set_parser(parser)
# # Supply the password for initialization.
# # (If no password is set, give an empty string.)
# doc.initialize(password)
# # Check if the document allows text extraction. If not, abort.
# if not doc.is_extractable:
#     raise PDFTextExtractionNotAllowed
# # Create a PDF resource manager object that stores shared resources.
# rsrcmgr = PDFResourceManager()
# # Create a PDF device object.
# device = PDFDevice(rsrcmgr)
# # Create a PDF interpreter object.
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# # Process each page contained in the document.
# for page in doc.get_pages():
#     interpreter.process_page(page)
# 
#==============================================================================
os.chdir("C://Users//aozgursuz//Downloads")
ac = open ( "Python Cookbook - David Beazley.pdf", "rb")
tara = PDFParser(ac)
belge = PDFDocument()
tara.set_document(belge)
belge.set_parser(tara)
kaynak = PDFResourceManager()
alet = PDFDevice(kaynak)
yorumla = PDFPageInterpreter(kaynak, alet)
for page in belge.get_pages():
     yorumla.process_page(page)
