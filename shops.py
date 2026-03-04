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
