import tkinter as tk
import time
import os
import random
f = open("C:\\Users\\magnu\\OneDrive\\Programering\\pyton\\tulleprosjekter\\Jklm\\jklm cheat 2\\dict.txt","r")

ord_liste=[]
root=tk.Tk()
root.withdraw()

for ord in f.readlines():
    ord=ord.replace("\n","")
    ord_liste.append(ord)

def finn_ord(v):
    liste_av_fungerende_ord=[]
    for x in ord_liste:
        if v in x:
            liste_av_fungerende_ord.append(x)
    return liste_av_fungerende_ord
def clipboard(text):
    cmd = 'echo | set /p nul=' + str(text) + '| clip'
    os.system(cmd)
clipboard("FE")  
x=root.clipboard_get()    
while True:
    if not(x==root.clipboard_get()):
        s=finn_ord(root.clipboard_get())
        if not(len(s)==0):
            x = s[random.randint(0,len(s)-1)]
            clipboard(x)  
        
    time.sleep(0.05)



 

