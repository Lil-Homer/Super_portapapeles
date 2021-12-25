#Super portapapeles
#Lil_Homer
#version=1.0
#2021-12-22



import pyperclip as pyp
from pynput import keyboard as kb
import time

memoria=["","",""]
portapapeles=""
marcador=0

def accion():
    global memoria
    global portapapeles
    global marcador

    if memoria[-1]=="'\\x04'" or memoria[-3:]==["Key.ctrl_l","Key.alt_l","'d'"]: #Ctrl + d
        portapapeles=""
        pyp.copy(portapapeles)
        if marcador==0:
            marcador=1
            print("MODO SUPERPORTAPAPELES ON")
        else:
            marcador=0
            print("MODO SUPERPORTAPAPELES OFF")
    elif memoria[-1]=="'\\x03'" or memoria[-1]=="'\\x18'" or memoria[-3:]==["Key.ctrl_l","Key.alt_l","'x'"]: #Ctrl + c o Ctrl + x
        if marcador==1:
            time.sleep(0.5)
            t = pyp.paste()
            portapapeles+=t
            pyp.copy(portapapeles)
    elif memoria[-1]=="'\\x06'" or memoria[-3:]==["Key.ctrl_l","Key.alt_l","'f'"]: #Ctrl + f
        portapapeles=""
        pyp.copy(portapapeles)
    elif memoria[-1]=="'\\x02'": #Ctrl + b
        print(portapapeles)
    elif memoria==["Key.ctrl_l","Key.alt_l","Key.delete"] or memoria==["Key.alt_l","Key.ctrl_l","Key.delete"] :
        exit
    else:
        pass

def actuar(tecla):
    memorizar(str(tecla))
    accion()
    

def memorizar(t):
    global memoria
    if not len(memoria)==3:
        memoria.append(t)
    else:
        if t in memoria[-1]:
            pass
        else:
            memoria=memoria[1:]
            memoria.append(t)


#Mensaje con imagen inicial y título
with open("inicio.txt","r",encoding="utf-8") as file:
    print(file.read())
with open("comandos.txt","r",encoding="utf-8") as f:
    print(f.read())
#
with kb.Listener(actuar) as escuchador:
    escuchador.join()  
