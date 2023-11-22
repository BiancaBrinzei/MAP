#12)Un program care sa afiseze numerele Fibonacci

n=int(input("\nIntrodu numarul:"))
j=1
i=1
s=0
print(i)
print(j)
while s<n:
    print (s)
    s=i+j
    i=j
    j=s