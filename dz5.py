l1 = 'python'
print(type(l1))
print(l1[::-1])

l2 = len(l1)
print(l2)

l4 = list(l1)
print(l4)

l5 = str(l4[2:len(l1):3])
print(l5)
print(type(l5))
print(l5.split('|'))
print('|'.join(l5))


def peretvorenna(a):
    d = {}
    for i in a:
        d[i] = a.count(i)
    print(d)


peretvorenna('jyjkkui')


def peretvorenna1(a):
    d = {}
    for i in a:
        d[i] = d.get(i, 0) + 1
    print(d)


peretvorenna1('jyjkkui2223')


def maxspisok(s1):
    for elem in s1:
        maxelem = 0
        if len(elem) > maxelem:
            maxelem = elem
    print(maxelem)


maxspisok(['gggg', 'jki', 'jjjkuuu'])


def sortspisok(a, b):
    c = a.split(b)
    c.sort()
    print(b.join(c))


sortspisok('d/a/g', '/')
sortspisok('d-b-g-q-a', '-')


def chislospisok(a):
    d = []
    for i in a:
        d.append(chr(i))
    print(d)


chislospisok([119, 101, 108, 108, 32, 100, 111, 110, 101])
