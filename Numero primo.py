num = 108
if num > 1:
    for i in range (2, num//2):
        #print(2, num//2)
        #print("-----------")
        #print(i)
        #print("-----------")
        #print(num%i)
        #print("###########")
        if (num%i) == 0:
            print (num, "NO es un numero PRIMO")
            break
        elif (i+1==num//2):
            print (num, "SI un numero PRIMO")