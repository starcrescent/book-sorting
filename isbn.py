import PyPDF2, os
os.chdir(r"C:\Users\Civanmerd\Desktop\pdf")
book=open('CNC Robotics_ Build Your Own Sh - Geoff Williams.pdf', 'rb')
bookreader = PyPDF2.PdfFileReader(book)
bookpage = bookreader.getPage(2)
sayfa = bookpage.extractText()
if 'ISBN' in sayfa:
    print ("true")

#print(sayfa)
#print (sayfa.encode('utf-8'))
