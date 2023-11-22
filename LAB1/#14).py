#14)Det cel mai mare si cel mai mic numar dintr o lista de numere citite de la tastatura

v=[]
s=0
max=0
min=0
n=int(input("\nNumarul de elemente din lista: "))
print("\n")
for i in range(n):
    valoare+int(input("Introdu v["+str(i)+"]:"))
    v.append(valoare)

    if v[i]>max:
        max=v[i]
    if v[i]<min or min==0:
        min==v[i]

print("\nCel mai mare numar din lista este",max)
print("Cel mai mare numar din lista ",min,".\n")