#Lamda (Nomsiz funksiya )
# Taminlovchi=Argument : Amallar
# kvadrat=lambda x :x*x
# son=int(input("Son kiriting : "))
# print(kvadrat(son))

# sonlar=range(1,50)
# def newdaraja(n):
#     return lambda x:x**n

# print("Istalganonning kubini chiqaruvchi funksiya")
# son =int(input("Son kiritng: "))
# natija=newdaraja(son)
# newdaraja(3)
# print(natija)

#Choise
# import random as r
# taomlar=["Osh","Manti","Shorva","Bugun ro'za"]
# tanla=r.choice(taomlar)
# print("Bugun ",tanla ,"yeymiz")


import random as r
print("BU mini o'yin . Ya'ni kompyuter bir son o'ylaydi , siz uni topishingiz kerak 1-10 gacha")
son=r.randint(1,10)
while True:
    inputson=int(input("Son kiriting : "))
    if son==inputson:
        print("To'g'ri topdingiz")
        break
    else:
        print("Xato")


    