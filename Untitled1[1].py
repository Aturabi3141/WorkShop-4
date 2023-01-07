#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    a = input("Bilgisayarınız Fişe takılı mı?y|n")
    if a == "n":
        print("Bilgisayarını fişe tak")
    elif a == "y":
        b = input("Başlatma düğmesine bastınız mı?y|n")
        if b == "n":
            print("Düğmeye basınız")
        elif b =="y":
            c = input("Bilgisayarınızın ışıkları ve sesi mevcut mu?y|n" )
            if c == "n":
                print("Sigortayı kontrol et")
            elif c=="y":
                d =input("Sigortaları çalışıyor mu?y|n")
                if d == "y":
                    print("Teknik servise basvurun")
                else: 
                    d == "n"
                    print("Sigortaları açıp tekrar deneyin!")

