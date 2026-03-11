# New file create

# with open("Newfile.txt","w") as file:
#     file.write("Salom Ibrohim")

# with open("Newfile.txt","a") as file:
#     file.write(".Xush kelibsan !")

# with open("Newfile.txt","r") as file:
#     salomlash=file.read()
# print(salomlash)
# import pickle

# birthday=input("Tug'ilgan sanangizni kiriting (04072005) : ")
# with open("pi_million_digits.txt") as pifile:
#     PI=pifile.read()
# if birthday in PI:
#     print("Bor")
# else:
#     print("Yoq")
# PI=PI.rstrip()
# PI=PI.replace('\n','')
# PI=PI.replace(' ','')
# PI=float(PI)
# with open("floatpinew.txt","wb") as file:
#     pickle.dump(PI,file)


name = input("Ismingizni kiriting : ")
lasname=input("Familiyangizni kiriting : ")
age=input("Yoshingizni kiriting : ")
with open('myinfo.txt','w') as myfile:
    for info in [name,lasname,age]:
        myfile.write(info +"\n")
hobbiy=input("Hobbiyingiz nima : ")
with open("myinfo.txt","a") as file:
    file.write(hobbiy+'\n')
with open('myinfo.txt','r') as file:
    readfile=file.read()
print(readfile)