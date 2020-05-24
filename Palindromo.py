num=int(input("Enter a number:"))
temp=num
rev=0
palin=0
while (num>0):
    dig=num%10
    #obtiene el ultimo numero de la variable num ------- saca el ultimo numero
    rev=rev*10+dig
    #Multiplica por 10 el 
    # ultimo valor de rev y le va aumntando el ultimo digito obtenido de num
    num=num//10
    #Eliminia el ultimo numero de la variable num actual --------- elimina el ultimo numero
    if(temp==rev):
        palin=1
if(palin==1):
    print("Es un palindromo")
else:
    print("No es un palindromo")