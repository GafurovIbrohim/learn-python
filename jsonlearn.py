#Json
import json

# data={"Model":"Malibu","Rang":"Qora","Narxi":20000,"Yili":2020}

# with open('car_json','w')as file:
#     json.dump(data,file)
# # print(data)
# # print(type(data))
# # data_json=json.dumps(data)
# # print(data_json)
# # print(type(data_json))

# talaba json
# talaba1={'ism':'Ibrohim','familiya':"G'afurov",'yosh':23,'bosqich':4}
# talaba2={'ism':'Alijon','familiya':"Valiyev",'yosh':22,'bosqich':3}
# talaba3={'ism':'Dilshod','familiya':"Choriyev",'yosh':20,'bosqich':1}

# talabalar=[talaba1,talaba2,talaba3]
# with open('newtalabajson.txt','w') as file:
#     json.dump(talabalar,file)

# # talaba_json=json.dumps(talaba)
# # print(talaba_json)
# # print(type(talaba_json))

# # qayta_oqi=json.loads(talaba_json)
# # print(type(qayta_oqi))
# # print(f"{qayta_oqi['ism']} {qayta_oqi['familiya']}")

# with open("newtalabajson.txt") as file:
#     qayt=json.load(file)
# for talaba in qayt:
#     print(f"{talaba['ism']} {talaba['familiya']} {talaba['yosh']} yoshda. U {talaba['bosqich']}-bosqich talabasi")


#wikipediya

with open('wiki.json') as info:
    newwiki=json.load(info)

title=newwiki['query']['pages']['13801']['title']
print(title)
exctrakt=newwiki['query']['pages']['13801']['extract']
print(exctrakt)