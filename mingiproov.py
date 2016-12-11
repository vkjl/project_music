import winsound
from random import randint


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
järjend = [c, cis, d, dis, e, f, fis, g, gis, a, ais, h]
# list = genereeri_helisid([c, d, e, f, g, a, h])


def genereeri_helisid(lst):
    uus_list = []
    for el in lst:
        juhuslik = randint(0, 6)
        a = lst[juhuslik]
        uus_list.append(a)

    return uus_list


def helide_muutja(lst):
    suvaline_element = randint(0, len(lst) - 1)
    suvaline = lst[suvaline_element]
    el_indeks_järjend = järjend.index(suvaline)
    if randint(0, 1) == 1:
        try:
            lst[suvaline_element] = järjend[el_indeks_järjend + 1]
        except:
            lst[suvaline_element] = järjend[el_indeks_järjend - 1]
    else:
        try:
            lst[suvaline_element] = järjend[el_indeks_järjend - 1]
        except:
            lst[suvaline_element] = järjend[el_indeks_järjend + 1]

    return lst


def mängib_niisama(lst):
    for el in lst:
        winsound.PlaySound(el, winsound.SND_FILENAME)


def korda_või_ära_korda_meloodiat(lst):
    if randint(0, 1) == 1:
        for el in lst:
            winsound.PlaySound(el, winsound.SND_FILENAME)
        # print("Sama.")
    else:
        uus_list = helide_muutja(lst)
        for el in uus_list:
            winsound.PlaySound(el, winsound.SND_FILENAME)
        # print("Erinev.")

"""
def kas_lõpetan_küsimused(küsimuse_kordaja1):
    global küsimuse_kordaja
    küsimuse_kordaja += 1
    if küsimuse_kordaja1 == 10:
        return lambda: raise_frame(last_frame)

    return raise_frame(question_frame)
"""

