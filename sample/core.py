# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
#import glob
import shutil

os.chdir("C://Users//aozgursuz//Downloads") #os.chdir("\\media\\WD4TB\\")

bas_dizin = os.getcwd()

#isimler = os.listdir(bas_dizin)

#print (isimler)

dizin_isimleri = [name for name in os.listdir(bas_dizin) if os.path.isdir(os.path.join(bas_dizin, name))]
print (dizin_isimleri)
                  
dosya_isimleri = [name for name in os.listdir(bas_dizin) if os.path.isfile(os.path.join(bas_dizin, name))]
print (dosya_isimleri)

for dosya in dosya_isimleri:
    if dosya.endswith(".pdf"):
        
#        shutil.move(dosya, "C://Users//aozgursuz//Downloads//deneme")#os.chdir("\\media\\WD4TB\\PDF")

#her bir kitabın başlığının ilk harfiyle başlayan dizine taşı. Baş harf ile
#başlayan dizin yoksa dizini oluştur. Dosya adı mevcut mu? Kontrol et. Mevcut
#sa "chift" adında dizin oluştur ve içine taşı. "chift" içinde dosya adı mevcut
#mu? Kontrol et. Mevcut sa "chift" adında dizin oluştur ve içine taşı...
        
#def get_hmm():
#    """Get a thought."""
#    return 'hmmm...'
#
#def hmm():
#    """Contemplation..."""
#    print get_hmm()
