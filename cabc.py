from tkinter import *
from tkinter import ttk
from random import randint

# funktsioonid

def alusta():
    # uuendab akent ja paiguteb sinna kaks play nuppu

    return


# muutujad
a = []
b = []

# tegelik algus
root = Tk()
root.title("Kõrva kontroll")

frame1 = Frame(root)

tervitus = ttk.Label(frame1, text="Tere tulemast!")
tervitus.grid(column=0, row=0, padx=10, pady=10, sticky=(N, W))

seletus = ttk.Label(frame1, text="""""")
seletus.grid(column=0, row=2, padx=10, pady=10, sticky=(E, W ))

start = ttk.Button(frame1, text="Alusta!", command=alusta())
start.grid(column=0, row=4, padx=10, pady=10)

frame1.columnconfigure(1, weight=1)
frame1.rowconfigure(1, weight=1)

frame2 = Frame(root)

play_nupp_a = ttk.Button(frame2, text="Esimene heli", command=mangib_niisama())
play_nupp_a.grid(column=0, row=0, padx=10, pady=10)

play_nupp_b = ttk.Button(frame2, text="Teine heli", command=mangi_meloodiat())
play_nupp_b.grid(column=1, row=0, padx=10, pady=10)

küsimus = tkk.Label(frame2, text="")



root.mainloop()