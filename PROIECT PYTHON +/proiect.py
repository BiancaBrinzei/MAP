import random

def genereaza_parola(length=8):
    litere = 'abcdefghijklmnopqrstuvwxyz'
    Litere = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numere = '0123456789'
    simboluri = '!@#$%^&*()_-+=<>?/'
    toate_caracterele = litere + Litere + numere + simboluri
    parola = ''.join(random.sample(toate_caracterele, length))
    return parola
def verifica_parola_puternica(parola):
    puternica = True

    if len(parola) < 8:
        puternica = False
        print("Parola trebuie să aibă cel puțin 8 caractere.")

    if not any(c in"abcdefghijklmnopqrstuvwxyz" for c in parola):
        puternica = False
        print("Parola trebuie să aibă cel puțin o literă mică.")

    if not any(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in parola):
        puternica = False
        print("Parola trebuie să aibă cel puțin o literă mare.")

    if not any(c in '0123456789' for c in parola):
        puternica = False
        print("Parola trebuie să aibă cel puțin o cifră.")

    if not any(c in '!@#$%^&*()-_+=<>?/' for c in parola):
        puternica = False
        print("Parola trebuie să aibă cel puțin un simbol.")

    if puternica:
        print("Parola este puternică.")
    else:
        print("Parola este slabă.")

parola_generata = genereaza_parola()
print("Parolă generată:", parola_generata)
verifica_parola_puternica(parola_generata)