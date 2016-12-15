import tkinter as tk
from tkinter import ttk
import winsound
from random import randint
import copy

# selle listi võiks panna dictionarisse
c = '39188_jobro_piano-ff-041 (mp3cut.net).wav'
cis = '39189_jobro_piano-ff-042 (mp3cut.net).wav'
d = '39190_jobro_piano-ff-043 (mp3cut.net).wav'
dis = '39191_jobro_piano-ff-044 (mp3cut.net).wav'
e = '39193_jobro_piano-ff-045 (mp3cut.net).wav'
f = '39194_jobro_piano-ff-046 (mp3cut.net).wav'
fis = '39195_jobro_piano-ff-047 (mp3cut.net).wav'
g = '39196_jobro_piano-ff-048 (mp3cut.net).wav'
gis = '39197_jobro_piano-ff-049 (mp3cut.net).wav'
a = '39198_jobro_piano-ff-050 (mp3cut.net).wav'
ais = '39199_jobro_piano-ff-051 (mp3cut.net).wav'
h = '39200_jobro_piano-ff-052 (mp3cut.net).wav'
noodiJärjend = [c, cis, d, dis, e, f, fis, g, gis, a, ais, h]


def genereeri_helisid(lst):
    # teeb heli listi noodiJärjendist

    uus_list = []
    for el in lst:# saaks teha ka inrange käsuga iseenesest
        juhuslik = randint(0, 6)
        a = lst[juhuslik]
        uus_list.append(a)

    return uus_list


def mängib_niisama(lst):
    for el in lst:
        winsound.PlaySound(el, winsound.SND_FILENAME)


def helide_muutja(lst):
    # muuda ühte suvalist elementi

    suvaline_element = randint(0, len(lst) - 1)
    suvaline = lst[suvaline_element]
    el_indeks_järjend = noodiJärjend.index(suvaline)

    if randint(1, 2) == 1:
        try:
            lst[suvaline_element] = noodiJärjend[el_indeks_järjend + 1]
        except:
            lst[suvaline_element] = noodiJärjend[el_indeks_järjend - 1]
    else:
        try:
            lst[suvaline_element] = noodiJärjend[el_indeks_järjend - 1]
        except:
            lst[suvaline_element] = noodiJärjend[el_indeks_järjend + 1]

    return lst


def korda_või_ära_korda_meloodiat(lst):

    if randint(0, 1) == 1:
        uus_list = lst

    else:
        uus_list = helide_muutja(lst)

    return uus_list


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MuutujaHoidja, AlgusLeht, MuusikaKuulamine1, MuusikaKuulamine2, MuusikaKuulamine3, MuusikaKuulamine4,
                  MuusikaKuulamine5, MuusikaKuulamine6, MuusikaKuulamine7, MuusikaKuulamine8,
                  MuusikaKuulamine9, MuusikaKuulamine10, TulemusLeht):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AlgusLeht)

        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", font=("Times New Roman", 15))
        style.configure("TButton", padding=5, relief="flat", font=("Times New Roman", 13), background="#ccc")


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MuutujaHoidja(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.shared_data = {
            "punktid": tk.IntVar()
        }


    def tulemus(self, heliSamasus, pakkumine):
        if pakkumine is heliSamasus:
            self.addone()

    def addone(self):
        punkt = self.shared_data["punktid"].get()
        print(punkt)
        punkt += 1
        self.shared_data["punktid"].set(punkt)
        print(self.shared_data["punktid"].get())


class AlgusLeht(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="""
Tere tulemast tegema muusikalise kuulmise testi. Testi käigus kuulete kahte viisijuppi.

Teie ülesandeks on aru saada, kas kuuldud helid olid samad või väikese erinevusega.
Vastavalt sellele peate vajutama nupule "Sama" või "Erinev". Head kuulamist!
""")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Alusta testi",
                             command=lambda: controller.show_frame(MuusikaKuulamine1))
        button1.pack()


class MuusikaKuulamine1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 1/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine2))
        button1.pack()


class MuusikaKuulamine2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 2/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine3))
        button1.pack()


class MuusikaKuulamine3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 3/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine4))
        button1.pack()


class MuusikaKuulamine4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 4/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine5))
        button1.pack()


class MuusikaKuulamine5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 5/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine6))
        button1.pack()


class MuusikaKuulamine6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 6/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine7))
        button1.pack()


class MuusikaKuulamine7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 7/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine8))
        button1.pack()


class MuusikaKuulamine8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 8/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine9))
        button1.pack()


class MuusikaKuulamine9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 9/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(MuusikaKuulamine10))
        button1.pack()


class MuusikaKuulamine10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, style="BW.TLabel", text="Küsimus 10/10")
        label.pack(pady=10, padx=10)

        heliList = genereeri_helisid(noodiJärjend)
        heliList2 = copy.deepcopy(heliList)
        heliList2 = korda_või_ära_korda_meloodiat(heliList2)

        onSama = False
        if heliList == heliList2:
            onSama = True

        button2 = ttk.Button(self, text="Esimene viis",
                             command=lambda: mängib_niisama(heliList))
        button2.pack()

        button3 = ttk.Button(self, text="Teine viis",
                             command=lambda: mängib_niisama(heliList2))
        button3.pack()

        button4 = ttk.Button(self, text="Sama",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, True))
        button4.pack()

        button5 = ttk.Button(self, text="Erinev",
                             command=lambda: self.controller.frames[MuutujaHoidja].tulemus(onSama, False))
        button5.pack()

        button1 = ttk.Button(self, text="Järgmine küsimus",
                             command=lambda: controller.show_frame(TulemusLeht))
        button1.pack()


class TulemusLeht(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label2 = ttk.Label(self, text="Te arvasite õigesti:")
        label2.configure(font=("Times New Roman", 14))
        label2.pack(pady=10, padx=10)

        self.label = tk.Label(self, textvariable=self.controller.frames[MuutujaHoidja].
                              shared_data["punktid"])
        self.label.configure(font=("Times New Roman", 14))
        self.label.pack(padx=10)

        label1 = ttk.Label(self, text="""
Muusikakeskus asub ajukoores parema kõrva kõrgusel oimusagaras.
Musikaalsuse spekter on väga lai, ulatudes absoluutsest kuulmisest
musikaalsuse täieliku puudumise ehk amuusiani, kui ei tunnetata
muusikalisi signaale.

On tõsi, et amuusia diagnoosiga inimesi saab õpetada muusikat tegema
teatud tehnika abil – harjutada nad pilli mängima või koos teistega
lihtsamaid viise laulma –, kuid musikaalsuse puudumist ehk amuusiat
ravida ei ole võimalik.

Muusika kuulamisel, loomisel ja esitamisel on kõige olulisem
otsene tunnetusprotsess. Muusika suudab kahtlemata tekitada tugevaid
emotsioone ja heaolutunnet, seda nii sel juhul, kui ise muusikat tehakse,
kui ka kuulamise korral.
""")
        label1.configure(font=("Times New Roman", 15))
        label1.pack()

        button1 = ttk.Button(self, text="Tagasi algusesse",
                             command=lambda: controller.show_frame(AlgusLeht))
        button1.pack(pady=20)


app = Application()
app.mainloop()
