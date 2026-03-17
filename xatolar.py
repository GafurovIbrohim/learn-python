#Xatolar bilan ishlash Try and except
yosh = input("Yoshingizni kiriting : ")
# if yosh.isdigit():
#     yosh=int(yosh)
#     print(f"Siz {2026-yosh}-yilda tug'ilgansiz ")
# else:
#     print("siz butun son kiritishingiz kerak edi !")
try:
    yosh=int(yosh)
except:
    print("Yoshga butun son kiritiladi . ")
else:
    print("To'gri")