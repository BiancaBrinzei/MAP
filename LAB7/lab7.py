import random
import matplotlib.pyplot as plt
from PIL import Image

piatra = Image.open("piatra.jpeg")
paper = Image.open("paper.png")
foarfeca = Image.open("foarfeca.png")

def arata_paralel(imagine1, imagine2):
    # Afișarea imaginilor în paralel
    fig, ax = plt.subplots(1, 2, figsize=(6, 2))
    
    ax[0].imshow(imagine1)
    ax[0].axis('off')
    ax[0].set_title('Utilizator')

    ax[1].imshow(imagine2)
    ax[1].axis('off')
    ax[1].set_title('Calculator')

    plt.show()

def obtine_alegere_utilizator():
    print("Alege: 1 - Piatră, 2 - Hârtie, 3 - Foarfecă")
    alegere_utilizator = input("Introduceți opțiunea dvs.: ")
    return int(alegere_utilizator)

def obtine_alegere_computer():
    return random.randint(1, 3)

def joc_piatra_hartie_foarfeca():
    alegere_utilizator = obtine_alegere_utilizator()
    alegere_computer = obtine_alegere_computer()

    imagine_utilizator = None
    imagine_calculator = None

    if alegere_utilizator == 1:
        imagine_utilizator = piatra
    elif alegere_utilizator == 2:
        imagine_utilizator = paper
    elif alegere_utilizator == 3:
        imagine_utilizator = foarfeca

    if alegere_computer == 1:
        imagine_calculator = piatra
    elif alegere_computer == 2:
        imagine_calculator = paper
    elif alegere_computer == 3:
        imagine_calculator = foarfeca

    arata_paralel(imagine_utilizator, imagine_calculator)

    rezultat = determina_castigator(alegere_utilizator, alegere_computer)
    print(rezultat)

def determina_castigator(alegere_utilizator, alegere_computer):
    print(f"Utilizatorul a ales:  {alegere_utilizator}")
    print(f"Calculatorul a ales: {alegere_utilizator}")

    if alegere_utilizator == alegere_computer:
        return "Egalitate!"
    elif (alegere_utilizator == 1 and alegere_computer == 3) or (alegere_utilizator == 2 and alegere_computer == 1) or(alegere_utilizator == 3 and alegere_computer == 2):
        return "Utilizatorul câștigă!"
    else:
        return "Calculatorul câștigă!"


joc_piatra_hartie_foarfeca()