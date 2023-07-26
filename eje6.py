contpar=0
contimp=0
op=1
n=0
while(op!=0):
    n=int(input("digite n\n"))
    if(n%2==0):
        contpar+1
    else:
        contimp+=1
        op=int(input("desea continuar 1/0 \n"))
        print("par",contpar,"impar",contimp)