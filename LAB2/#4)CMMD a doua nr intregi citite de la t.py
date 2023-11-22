#4)CMMD a doua nr intregi citite de la tastatura

a=int(input("Introduceti a:"))
b=int(input("Introduceti b:"))
while b!=0:
    r=a%b
    a=b
    b=r
print(a)
