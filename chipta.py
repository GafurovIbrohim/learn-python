print("Muzayg kirish chipta narxlari 7 yoshgacha 2000 7-16 yoshlarga 3000 , 16-65 yoshlarga 5000, 65 dan kattalarga tekin ...")
ishora=True
while ishora:
    add=input("Yana chipta olishni istaysizmi (ha/yoq) : ")
    if add!='yoq':
        age=int(input("Yoshingizni kiriting : "))
        if age<7 :
            print("Chipta narxi 2000 som")
        elif age>=7 and age<=16 :
            print("Chipta narxi 3000 som")
        elif age>16 and age<=65:
            print("Chipta narxi 5000 som")
        else:
            print("Chipta bepul")
    else:
        ishora=False