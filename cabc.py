from tkinter import *
from tkinter import ttk
from random import randint
def alusta():
    # uuendab akent ja paiguteb sinna kaks play nuppu


    play_nupp_a = ttk.Button(raam, text="Esimene heli", command=mangi_heli(a))
    play_nupp_a.grid(column=0, row=0, padx=10, pady=10)
    play_nupp_b = ttk.Button(raam, text="Teeine heli", command=mangi_heli(b))
    play_nupp_b.grid(column=1, row=0, padx=10, pady=10)
    return

def küsimus():
    # ??A
    return

def mangi_heli(heli):

    return

raam = Tk()
raam.title("Kõrva kontroll")

tervitus = ttk.Label(raam, text="Tere tulemast ")
tervitus.grid(column=0, row=0, padx=10, pady=10, sticky=(N, W))

seletus = ttk.Label(raam, text="""""")
seletus.grid(column=0, row=2, padx=10, pady=10, sticky=(E, W ))

start = ttk.Button(raam, text="Alusta!", command=alusta)
start.grid(column=0, row=4, padx=10, pady=10)

raam.columnconfigure(1, weight=1)
raam.rowconfigure(1, weight=1)

raam.mainloop()
