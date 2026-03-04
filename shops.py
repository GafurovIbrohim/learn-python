# print("Bu yerga siz yaxshi ko'rgan kitoblaringizni yozasiz")
# fovoritebooks=[]
# ishora=True
# while ishora :
#     book=input("Yaxshi ko'rgan kitobingizni kiriting (Agar tugagan bo'lsa stop so'zini kiriting !) : ")
#     if book=='stop':
#         break
#     else:
#         fovoritebooks.append(book)
# print("Siz yoqtiradigan kitoblar royxati : ",fovoritebooks)


# print("Muzayg kirish chipta narxlari 7 yoshgacha 2000 7-16 yoshlarga 3000 , 16-65 yoshlarga 5000, 65 dan kattalarga tekin ...")
# ishora=True
# while ishora:
#     add=input("Yana chipta olishni istaysizmi (ha/yoq) : ")
#     if add!='yoq':
#         age=int(input("Yoshingizni kiriting : "))
#         if age<7 :
#             print("Chipta narxi 2000 som")
#         elif age>=7 and age<=16 :
#             print("Chipta narxi 3000 som")
#         elif age>16 and age<=65:
#             print("Chipta narxi 5000 som")
#         else:
#             print("Chipta bepul")
#     else:
#         ishora=False

    
print("Buyurtma qabu qilish")
orders=[]
while True:
    order=input("Buyurtma bering  yoki (stop) ni kiritng : ")
    if order.lower()!='stop':
         orders.append(order)
    else:
         break
print("Sizning buyurtmalaringiz : ", orders)

print("E-BOZOR")
products={}
while True:
    want=input("Mahsulot kiritishni hohlaysizmi (ha, yoq) : ")
    if want.lower()!='yoq':
        product=input("Maxsulot kiriting : ")
        price=float(input("Narxini kiriting : "))
        products[product]=price
    else:
        break
print("Maxsulotlar royxati :",products)

for product in orders:
    if product in products:
        print(f"{product} E-bozorda bor va uning narxi : {products[product]}")
