#16) Ecuatia de gr2

a=int(input("\nIntrodu a="))
b=int(input("Introdu b="))
c=int(input("Introdu c="))

s=b*b-4*a*c
if s==0:
    x1=-b/2*a
    print("\nSolutia ecuatiei este: ",x1,".\n")
else:
    x1=(-b+s)/2*a
    x2=(-b-s)/2*a
    print("\nSolutiile ecuatiei sunt: ",x1," si ",x2,".\n")