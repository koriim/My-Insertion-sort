#Sequential Search
found=bool()
Array1=[21,15,90,18,18,10,11,105,6,11]
x=int(input("please enter the search no.:"))
for k in range(len(Array1)):
    if (found!=True and k==len(Array1)-1 ):
        print(x ," not found")
    elif(x==Array1[k]):
        print(k,Array1[k])
        found=True
