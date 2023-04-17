def f1(*a):
    assert isinstance(a, tuple)
    return list(a)


print(f1(10, 12, 15, 10))


def f2(**a):
    assert isinstance(a, dict)
    print(len(a))
    if 'user_type' in a:
        print(a['user_type'])
    else:
        print("Student")
    return a


f2(user_type='admin', ima='Oksana', curs='python')
f2(user='admin', ima='Oksana', curs='python')


def f3(*a, *b, c, d, /, e=2, f=5):
    pass


def f4(a):
    def f5(b):
        return a * b

    return f5


print(f4(2)(3))


def kvdrat(a):
    print('*****')
    a = a - 1
    if a != 0:
        kvdrat(a)
    else:
        return kvdrat


kvdrat(5)
