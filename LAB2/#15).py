#15)Sortati un vector de 8 elemente citite de la tastatura, met. Bubble Sort

v=[7]
print("\n")
for i in range(8):
    valoare = int(input("Introdu v["+str(i)+"]:"))
    v.append(valoare)
for i in range(8):
    swapped = False
    for j in range(0,7-i):
        if v[j]>v[j+1]:
            v[j],v[j+1]=v[j+1],v[j]
            swapped=True
    if not swapped:
        break
print("\nVectorul sortat este:",v,".\n")