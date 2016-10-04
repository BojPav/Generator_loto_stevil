print "<---Generatot Loto Stevil--->"

list_stevilke = []

st_stevilka = raw_input("Koliko stevil boste nakljucno generiral ?(1 - 10): ")

st_stevilka = int(st_stevilka)

import random

while len(list_stevilke) < st_stevilka:

    nova_stevilka = random.randint(1, 50)

    list_stevilke.append(nova_stevilka)

print " "
print "Vase loto stevilke: " + str(list_stevilke)