def max_chislo(a,b):
    if a > b:
        print('max chislo ravno', a)
    elif b > a:
        print('max chislo ravno', b)
    else:
        print('chisla ravni')
max_chislo(5,10)
max_chislo(5,3)
max_chislo(5,5)


def min_chislo(a,b,c):
    if a <= b and a <= c:
        print('min chislo ravno', a)
    elif b <= a and b <= c:
        print('min chislo ravno', b)
    elif c <= b and c <= a:
        print('min chislo ravno', c)

min_chislo(5,10,3)
min_chislo(5,1,45)
min_chislo(5,5,6)


def modul_chislo(a):
    print(abs(a))

modul_chislo(3)
modul_chislo( - 5)


def summa_chisel(a,b):
    print(a + b)
summa_chisel( - 4,5)
summa_chisel(10,3)


def znak_chisla(a):
    if a > 0:
        print('chislo dodatne')
    elif a < 0:
        print('chislo vid`emne')
    else:
        print('vvedeno chislo 0')
znak_chisla(5)
znak_chisla( - 5 )
znak_chisla(0)

