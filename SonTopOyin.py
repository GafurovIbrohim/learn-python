# Amaliy mashg'ulot 
#Son topish o'yini 
import random as r
print("Assalomu alaykum ! Bu o'yin kompyuter va sizning o'rtangizda bo'ladi . Birinchi kompyuter bir son o'ylaydi . Siz topasiz.\nKeyin siz bir son oylaysiz kompyuter topadi .")
name=input("Ismingizni kiriting : ")

def sontop():
    kompson=r.randint(1,50)
    sizurundingiz=0
    while True:
        sizurundingiz+=1
        son=input("Kompyuter son o'yladi . Taxminingizni kiriting(1-50) :")
        if son.isdigit():
            son=int(son)
        else : 
            print("Butun son kiriting !")
            continue
        
        if kompson==son:
            print("Siz to'g'ri topdingiz . ")
            break
        elif son>kompson:
            print("Kompyuter o'ylagan sondan katta son kiritdingiz !")
        elif son<kompson:
            print("Kompyuter o'ylagan sondan kichik son kiritdingiz ")
    return sizurundingiz

def sontopaman():
    print("Endi siz bir son o'ylang . Kompyuter uni topadi (1-50)")
    kompurundi=0
    ishora=1
    ishora2=50
    while True:
        kompurundi+=1
        if ishora>ishora2:
            print("Xatolik")
            break
            
        son=r.randint(ishora,ishora2)
        javob=input(f"Siz o'ylagan son {son} mi . Agar siz o'ylagan son to'g'ri bo'lsa (T)\nkattaroq bo'lsa (+). Kichikroq bo'lsa (-) kiriting : ")
        if javob.lower()=='t':
            print("Kompyuter to'g'ri topdi ")
            break 
        elif javob=="+":
            ishora=son+1
        elif javob=="-":
            ishora2=son-1
        else:
            print("Xatolik ")    
    return kompurundi


sizurundingiz=sontop()
kompurundi=sontopaman()
print(f"Siz {sizurundingiz} urunishda topdingiz . Komputer {kompurundi} urunishda topdi  ")
if sizurundingiz < kompurundi:
    print(f"Tabriklayman {name.title()} siz yutdingiz .")
else:
    print(f"Afsuski Komputer yutdi .")

