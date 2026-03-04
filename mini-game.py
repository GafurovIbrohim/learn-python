import random as r
print("BU mini o'yin . Ya'ni kompyuter bir son o'ylaydi , siz uni topishingiz kerak 1-10 gacha")
while True:
    son=r.randint(1,10)
    inputson=int(input("Son kiriting : "))
    if son==inputson:
        print("To'g'ri topdingiz")
        startgame=input("Yana o'ynashni hohlaysizmi (ha/yoq)")
        if startgame.lower()=='yoq':
            break
    else:
        print("Xato")
print("The end")

