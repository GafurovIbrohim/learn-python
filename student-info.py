# Studenlar malumotlarini kiriuvchi funksiya istalgancha malumot kiritsa boladi . 

#  def studentinfo(name,surname,**addinfo):
#     newinfo={}
#     newinfo['Ism']=name
#     newinfo['Familiya']=surname
#     for i in addinfo:
#         newinfo[i]=addinfo[i]
#     return newinfo

# name=input("Talabaning ismini kiriting : ")
# surname=input("Talabaning familiyasini kiriting : ")
# addinfo={}
# while True:
#     ishora=input("Yana malumot kiritishni istaysizmi (ha/yoq):" )
#     if ishora!='yoq':
#         key=input("Kalit kiriting :")
#         value=input("Qiymat kiriting : ")
#         addinfo[key]=value
#     else:
#         break

# print("Talaba haqida malumotlar : ",studentinfo(name,surname,**addinfo))