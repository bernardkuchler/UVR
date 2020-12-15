import math
math.sin

def get_i():
    combs = set()
    for vrstica in open("input.txt"):
        vrstica = vrstica.split()
        sp, zg = vrstica[0].split('-')
        crka = vrstica[1].replace(':', '')
        geslo = vrstica[2]
        vr = (int(sp), int(zg), crka, geslo)
        combs.add(vr)
    return combs


def count(combs):
    stev = 0
    for sp, zg, crka, geslo in combs:
        if sp <= geslo.count(crka) <= zg:
            stev += 1
    return stev


def count2(combs):
    stev = 0
    for sp, zg, crka, geslo in combs:
        if sp-1 < len(geslo) and zg-1 < len(geslo):
            if (geslo[sp - 1] == crka[0] and geslo[zg - 1] != crka[0]) or (geslo[sp - 1] != crka[0] and geslo[zg - 1] == crka[0]):
                stev += 1
    return stev


combs = get_i()
print(count(combs))
print(count2(combs))
