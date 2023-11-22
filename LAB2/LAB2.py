import pyautogui
import keyboard
import time
def  cautare_google():
    if pyautogui.locateOnScreen(r"C:\imagini\search.png",confidence=0.7)!=None:
        camp_google= pyautogui.locateOnScreen(r"C:\imagini\search.png",confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(5)
        pyautogui.write("Franta")
        pyautogui.press('enter')
        time.sleep(2) 

response = pyautogui.confirm("Doriti sa incepeti rularea programului?","Confirmare")
if (response =="OK"):
    cautare_google()
else:
    pyautogui.alert("Ati ales Anulare","Anulare")