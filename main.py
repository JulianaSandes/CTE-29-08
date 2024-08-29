from delta1 import delta
from raizes import raiz

a=int(input("Informe a: "))
b=int(input("Informe b: "))
c=int(input("Informe c: "))

d=delta(a,b,c)

print("O delta é: ",d)

if(d<0):
    print("Não existem raízes reais! ")
elif(d==0):
    x=raiz(a,b,d)
    print("Há uma única raiz, que vale :",x[0])
else:
    x=raiz(a,b,d)
    print("As raízes são: ",x)