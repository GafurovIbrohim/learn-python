# datetime
import datetime as dt
import re
data=dt.datetime.now()
today=data.date()
#,,,
# today=data.date()
# farq=dt.timedelta(days=14)
# for i in range(10):
#     print(today)
#     today=today+farq
    
#,,,
# hayit=dt.date(2026,3,20)
# qolgan_kun=hayit-today
    
# print(qolgan_kun)



# # Men yashagan kun 
# year=int(input("Tug'ilgan yilingizni kiriting :"))
# month=int(input("Tug'ilgan oyingizni kiriting : "))
# day=int(input("Tug'ilgan kuningizni kiriitng : "))
# birthday=dt.date(year,month,day)

# result=today-birthday
# print(f"Siz {result} kun yashagansiz .")

# text = "Narxlar 12000 som va 35000 som 23"
# natija=re.match("^N.....r",text)
# print(natija)


# Telefonni tekshirish 
####https://ihateregex.io/expr/e164-phone/
# telnumber=input("Telefon raqamingizni kiriting : ")
# andoza=r'^\+[1-9]\d{1,14}$'

# result=re.match(andoza,telnumber)
# print(result)



#web search

text="Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"
andoza=r'https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'

sahifalar=re.findall(andoza,text)
print(sahifalar)