def max_chislo(a, b):
    if a > b:
        return a
    else:
        return b


print(max_chislo(5, 19))
print(max_chislo(7, 3))
print(max_chislo(6, 6))


def min_chislo(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    return c


print(min_chislo(7, 10, 3))
print(min_chislo(6, 1, 5))
print(min_chislo(5, 5, 2))


def modul_chislo(a):
    if a > 0:
        return a
    else:
        return -a


print(modul_chislo(3))
print(modul_chislo(-5))


def summa_chisel(a, b):
    print(a + b)


summa_chisel(-4, 5)
summa_chisel(10, 3)


def znak_chisla(a):
    if a > 0:
        print('chislo dodatne')
    elif a < 0:
        print('chislo vid`emne')
    else:
        print('vvedeno chislo 0')


znak_chisla(5)
znak_chisla(-5)
znak_chisla(0)

