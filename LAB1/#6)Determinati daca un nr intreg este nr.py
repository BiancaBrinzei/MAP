#6)Determinati daca un nr intreg este nr prim

n=int(input("\nNumar:"))
OK=0
i=2
for i in range(2,n//2+1):
    if(n%i==0):
        OK=1
if(OK==0):
    print("Numarul ",n," este prim.")
else:
    print("Numarul ",n," nu este prim.\n")