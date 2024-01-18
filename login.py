from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import pyperclip
import os
import subprocess
import time
import shutil
import psutil


usuario_MM = "489JMP01"
password_MM = "AnbQYgLy"
usuario_R = "075JMP01"
password_R = "hAxmn7Dr"
usuario_EKT = "056JMP01"
password_EKT = "jpaMQnTz"
nombre_agente = "David Pinedo Dulanto" 
telefono_movil = 693941337
telefono_fijo = 918318958
# provincia leer del excel Altas SUC
# codigoMIGA leer del excel Altas SUC
check_box = "RED DISPERSION POSTES"
email = "gestion.telefonica@masmovil.com"
# plano = pedf carpeta compartida
# Tupla entre postes y IPDID_ID

def loginUser():
    #Condición para leer el nombre del excel guardado en la carpeta compartida.
    try:
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        driver.get("https://sgo.telefonica.es/v1/loginMarco")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write('489JMP01')
        pyautogui.press('tab')
        pyautogui.write('AnbQYgLy')
        pyautogui.press('tab')
        pyautogui.press('enter')
    except NoAlertPresentException:
        print(f"No se ha encontrado ninguna alerta en la página ----------------------------------------------")
    except NoSuchElementException:
        print(f"No se ha encontrado el elemento deseado ------------------------------------------------------")
    except IndentationError:
        print(f"El código esta mal identado ------------------------------------------------------------------")
    pass

def exitUser():
    try:
        texto_a_buscar = "Desconectar"
        elemento = driver.find_element(By.XPATH, f"//*[contains(text(), '{texto_a_buscar}')]")    
        # Hacer click en el elemento
        elemento.click()
        driver.implicitly_wait(5)
    except:
        print(f"No se ha encontrado el div para Desconectar")
    finally:
        driver.quit()

def procesoSUC():
    #No puede añadir integers
    driver.get("https://sgo.telefonica.es/v1/controlMarco?S=cuIrAltaSoliSUC&ultimoClick=cuIrAltaSoliSUC")
    pyautogui.press('tab')
    pyautogui.write(nombre_agente)
    pyautogui.press('tab')
    pyautogui.write(telefono_movil)
    pyautogui.press('tab')
    pyautogui.write(email)
    pyautogui.press('tab')
    pyautogui.write(telefono_fijo)
    time.sleep(15)
    #pyautogui.write('hOLA')
    pass

def leerExcel():
    #Función que recoge datos del excel Altas SUC.xls y lo transforma en una instancia de la clase Poste(definir)
     
    pass

# Inicializar el navegador
driver = webdriver.Chrome()
loginUser()
time.sleep(8)
#procesoSUC()
#Funcion sesion cerrar.
exitUser()

 
 