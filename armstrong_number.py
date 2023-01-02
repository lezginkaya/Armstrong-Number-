def armstrong(num):
    num_str=str(num)
    liste=[]
    n=0
    for n in range(0,len(num_str),1):
        liste.append(num_str[n])
    liste=list(map(int,liste))
    x=0
    for i in liste:
        x+=i**len(liste)
    if x==num:
        print(num, "armstrong sayısıdır")
    else:
        print(num,"armstrong sayısı değildir")
armstrong(153)







