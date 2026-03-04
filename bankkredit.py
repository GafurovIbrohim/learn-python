#bank
age=int(input("Yoshingizni kiriting : "))
monthmoney=float(input("Oylik daramadingiz qancha :"))
kredithistory=input("Kredit tarixingiz yaxshimi(ha/yoq): ")
if kredithistory=="yoq":
    print("Sizning kredit tarixingiz yomon . Sizga kredit bera olmaymiz !")
elif monthmoney>10000000:
    print("Tastiqladi")
elif monthmoney <3000000:
    print("Sizning oylik daromadingiz yetmaydi !")
elif age<21 or age>60:
    print("Yoshingiz togri kelmadi . ")
else :
    print("Sizga kredit ajratildi ")