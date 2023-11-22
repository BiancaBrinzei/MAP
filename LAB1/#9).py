#9) Un program care sa determine daca un an citit de la tastatura este un an bisect

n=int(input("Introdu anul:"))

if n%4==0:
    print("Anul ",n," este bisect.\n")
else:
    print("Anul ",n," nu este bisect.\n")