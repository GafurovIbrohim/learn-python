print("Salom restoranimizga xush kelibsiz . Bizda shirin va esda qolarli taomlar menyusi bor .")
menu={"osh":30000,"shashli":20000,"xonim":15000,"pepsi":20000}
order={}

number=int(input("Nechta taom buyurtma qilmoqchisiz : "))
for i in range(number):
    food=input(f"{i+1}- taomni kiriting : ")
    if food in menu:
       order[food]=menu[food]
    else:
        print("Bizda bunday taom yo'q")
print(f"Siz {list(order.keys())} ovqatlarni buyurtma qildingiz . Narxi : {sum(order.values())}")