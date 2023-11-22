#13)Un program care sa determine suma si media unei liste de numere citite de la tastatura

v=[]
n=int(input("\nNumarul de elemente din lista: "))
s=0

for i in range(n):
    valoare= int(input("Introdu v["+str(i)+"]:"))
    v.append(valoare)
    s=s+v[i]

m=s/n
print("\nSuma elementelor din lista este",s,".")
print("Media elementelor din lista este",m,".")
