# 1-kun

#print("Backend challange 60 kun")

# print("Salom bu sonning kvadarati va kubini hisoblovchi dastur ")
# son=int(input("Sonni kiriting : "))
# print(son, "ning kvadrati : " , son**2)
# print(son, "ning kubi : " ,son**3)

# name=input("Ismingizni kirting :")
# age=int(input("Yoshingizni kiriting :"))
# print(f"Salom {name} ! Sening tug'ilgan yiling : {2026-age}")

# #list
# # bozorlik=["olma" , "kartoshka","piyoz","guruch"]
# # print("Olinishi kerak bo'lgan maxsulotlar :", bozorlik)
# # bozorlik.append("Asal")
# # print(bozorlik)
# # bozorlik.reverse()
# # print(bozorlik)
# # bozorlik.sort()
# # print(bozorlik)
# # bozorlik.sort(reverse=True)
# # print(bozorlik)
# # bozorlik.remove("piyoz")
# # print(bozorlik)
# # mahsulot=bozorlik.pop(0)
# # print(bozorlik)
# # del bozorlik[2]
# # print(bozorlik)
# # bozorlik.insert(1,"Banan")
# # print(bozorlik)
# # print(len(bozorlik))

# # juft=list(range(120,1200,2))
# # print(juft)
# # yigindi=sum(juft)
# # print(yigindi)
# # minimum=min(juft)
# # maximum=max(juft)
# # ayirma=maximum-minimum
# # print(f"Eng katta son {maximum} dan , eng kichik son {minimum} ni ayirsa . Natija :  {ayirma}")

# # print(juft[0:20])
# # print(juft[-20:-1])

# taomlar=[]
# taomlar.append("Palov")
# taomlar.append("Manti")
# taomlar.append("Norin")
# taomlar.append("choy")
# taomlar.append("Shashlik")
# print(taomlar)
# taomlar2=taomlar[:]
# taomlar2.append("Mastava")
# print(taomlar2)
# taomlar2=tuple(taomlar2)
# print(taomlar2)

#for

# # friends=["Sanjar","Baxtiyor","Jamshid","Shaxruz","Ibrohim"]
# # repeat=0
# # for dost in friends:
# #     print(f"Hurmatli {dost} seni ertaga bo'lib o'tadigan ziyofatga taklif etaman ! ")
# #     repeat+=1
# # print(f"Kod {repeat} marotaba takrorlandi ")

# # toqnumbers=[]
# # for son in range(11,100,2):
# #     toqnumbers.append(son)
# # print(toqnumbers)  
# # for son in toqnumbers:
# #     print(f"{son} ning kubi: {son**3}")  

# print("Salom bugun nechta odam bilan uchrashding :")
# meets=[]
# members=int(input("Nechta : "))
# for member in range(members):
#     name=input(f'{member+1}-odamning ismini kiriting:')
#     meets.append(name)
# print(f"Sen bugun uchrashgan odamlar : {meets}")



#if

# blacklist=["Sanjar", "Ali","Vali"]
# name=input("Ismingiz nima : ")
# age=int(input("Yoshingiz nechchida : "))
# money=float(input("Qancha pulingiz bor : "))
# if age>18 and money>=5000 and name not in blacklist:
#     print("Ruxsat kirishga")
# else:
#     print("Kirishga ruxsat yo'q")


#bank
# age=int(input("Yoshingizni kiriting : "))
# monthmoney=float(input("Oylik daramadingiz qancha :"))
# kredithistory=input("Kredit tarixingiz yaxshimi(ha/yoq): ")
# if kredithistory=="yoq":
#     print("Sizning kredit tarixingiz yomon . Sizga kredit bera olmaymiz !")
# elif monthmoney>10000000:
#     print("Tastiqladi")
# elif monthmoney <3000000:
#     print("Sizning oylik daromadingiz yetmaydi !")
# elif age<21 or age>60:
#     print("Yoshingiz togri kelmadi . ")
# else :
#     print("Sizga kredit ajratildi ")


 # Dictonory (lug'at)

# brotherinfo={"name":"Botir" , "age":32, "t-yil":2000}
# print(f"Akamning ismi {brotherinfo['name']} u {brotherinfo['age']} yoshda . Akam {brotherinfo['t-yil']} da tug'ilgan  ")

# family={}
# member=int(input("Oilangizda nechta odam bor : "))
# for number in range(member):
#     person=input(f"Oilangizdagi {number+1} - odamning ismini kiriting :")
#     food=input(f"{person}ning sevimli taomini kiriting : ")
#     family[person]=food
# for k,q in family.items():
#     print(f"{k} ning sevimli taomi {q}")


# lugat={"integer":"Bu butun sonlar","float":"Bu kasr ko'rinishidagii sonlar","booleon":"Bu mantiqiy operatsiyalar"}
# word=input("Pythonda o'zgaruvchi turlarini kiriting  : ")
# print(lugat.get(word, "Bunday o'zgaruvchi yo'q"))

# dictonary={"integer":"Bu butun sonlar","float":"Bu kasr ko'rinishidagii sonlar","booleon":"Bu mantiqiy operatsiyalar"}
# for k , q in dictonary.items():
#     print(f"{k} ning manosi : {q}")

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}
# country=input("Davlat nomini kiriting : ")
# if country in davlatlar:
#     print(davlatlar[country])


# Navoiy={"Ism":"Alisher Navoiy","T-yili":1441,"T-joyi":"Hirot"}
# Bobur={"Ism":"Zahiriddin Muhammad Bobur ", "T-yili":1456 , "T-joyi": "Samarqand"}
# Beruniy={"Ism":"Beruniy","T-yili":None,"T-joyi":"Buxoro"}
# Karimov={"Ism":"Islom Karimov ", "T-yili":1936 , "T-joyi": "Samarqand"}

# fomouspersons=[Navoiy,Bobur,Beruniy,Karimov]


# Navoiy['Asar']="Xamsa"
# Bobur['Asar']="Boburnoma"
# Beruniy["Asar"]="Geometriya"
# Karimov["Asar"]="Yuksak manaviyat yengilmas kuch "

# for person in fomouspersons:
#     print(f"{person['Ism']} ning asarlaridan biri bu {person['Asar']} hisoblanadi . ")


# friends=int(input("Sening nechta dosting bor"))
# likekino={}
# for i in range(friends):
#     name=input(f"{i+1}-do'stingizni ismini kiriting : ")
#     print(f"{name} yoqtiradigan 3 ta kinosini kiritishingiz kerak .")
#     kinolar=[]
#     for k in range(3):
#        kino=input(f"{k+1}-kinoni kiriting : ")
#        kinolar.append(kino)
#     likekino[name]=kinolar

# for name in likekino:
#     print(f"{name} ning yoqtirgan kinolari : {likekino[name]}")


davlatlar={"Uzbekiston":{"Poytaxti":"Toshkent","Millati":"Uzb"},"Qozoqiston":{"Poytaxti":"Dushanbe", "Millati":"Qozoq"}}
print("Salom bu yerda sizni qiziqtirgan davlat haqida malumot olishingiz mumkin . ")
country=input("Sizga qaysi davlat haqida malumot kerak : ")
if country in davlatlar:
    print(f"{country}ning poytaxti : {davlatlar[country]['Poytaxti']}")
    print(f"{country}ning millati : {davlatlar[country]['Millati']}")
else:
    print("Lugatimizda bunday davlat yo'q")

    
