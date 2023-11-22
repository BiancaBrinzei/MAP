#5)Factorialul unui numar intreg citit de la tastatura

n=int(input("\nNumar: "))
a=1
for i in range(1,n+1):
    a*=i

print( "Factorialul numarului ",n," este ",a,".\n")