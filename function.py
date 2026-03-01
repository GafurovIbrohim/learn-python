# # Function 
# def helloword(ism):
#     """BU funksiya salomlashish funksiyasi . """
#     print("Hello world ! ")
#     print(f"Salom {ism.title()}")
# helloword('Ibrohim')


# def birthyear(name,age,nowyear):
#     print(f"Salom {name.title()} sening tug'ilgan yiling : {nowyear-age}")

# name=input("Ismingizni kiriting : ")
# age=int(input("Yoshingizni kiriting : "))
# nowyear=int(input("Hozirgi yilni kiriting : "))
# birthyear(name,age,nowyear)

# def generatefunc(son):
#     if son%2==0:
#         print("Juft son kiritdingiz ")
#     else:
#         print("Toq son kiritdingioz .")
# son=int(input("Son kiriting : "))
# generatefunc(son)



# def generateqoldiq(son):
#     for i in range(2,11):
#         if son%i==0:
#             print(f"{son} {i} soniga qoldiqsiz bo'linadi .")
#         else:
#             print(f"{son} {i} soniga qoldiqsiz bo'linmaydi .")
# number=int(input("son kiriting : "))
# generateqoldiq(number)


 #moslashuvchan funcsiyalar

# def dicts(*son):
#     dictresult=1
#     for i in son:
#         dictresult=dictresult*i
#     return dictresult

# sonlar=[]

# while True:
#     son=input("Son kiriting (hisoblash uchun * ni bosing ): ")
#     if son!="*":
#         son=int(son)
#         sonlar.append(son)
#     else:
#         break
# print(dicts(*sonlar))

#Studentinfo 

def studentinfo(name,surname,**addinfo):
    newinfo={}
    newinfo['Ism']=name
    newinfo['Familiya']=surname
    for i in addinfo:
        newinfo[i]=addinfo[i]
    return newinfo

name=input("Talabaning ismini kiriting : ")
surname=input("Talabaning familiyasini kiriting : ")
addinfo={}
while True:
    ishora=input("Yana malumot kiritishni istaysizmi (ha/yoq):" )
    if ishora!='yoq':
        key=input("Kalit kiriting :")
        value=input("Qiymat kiriting : ")
        addinfo[key]=value
    else:
        break

print("Talaba haqida malumotlar : ",studentinfo(name,surname,**addinfo))