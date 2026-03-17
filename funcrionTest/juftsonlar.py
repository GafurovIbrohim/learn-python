def selectjuftsonlar(sonlar):
    newsonlar=[]
    for son in sonlar:
        if son%2==0 :
            newsonlar.append(son)
    return newsonlar
