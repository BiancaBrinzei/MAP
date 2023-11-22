#17) Se citesc 3 nr de la tastatura, sa se afiseze daca aceste pot reprezenta unghiurile unui triunghi

a=int(input("\nIntrodu primul numar:"))
b=int(input("\nIntrodu al doilea numar:"))
c=int(input("\nIntrodu al treilea numar:"))
if (a+b+c)==180:
    print("Numerele ",a,",",b,"si",c," pot fi unghiurile unui triunghi.\n")