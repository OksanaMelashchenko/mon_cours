import random
import os
from collections import Counter
import string
from collections import OrderedDict


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            res1 = []
            for i in range(attempts):
                res = func(*args, **kwargs)
                if type(res) is not list:
                    res1.append(res)
                else:
                    res1.extend(res)
                if res1 == desired_value:
                    print('resultat dostignut', res1)
                    break
                # print('res1=', res1, 'desired_value', desired_value)
            if res1 != desired_value:
                print('resultat ne dostignut, res1=', res1, 'desired_value=', desired_value)
            return res1
        return inner_wrapper
    return wrapper

@retry(desired_value=3)
def get_random_value_with_default_attempts():
    return random.choice((1, 2, 3, 4, 5))

#@retry(desired_value=[1, 2])
def get_random_values_with_default_attempts(choices, size=2):
    return random.choices(choices, k=size)

@retry(attempts=7, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))

@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)

get_random_value()
get_random_value_with_default_attempts()
get_random_values_with_default_attempts([1, 2, 3, 4])
get_random_values_with_default_attempts([1, 2, 3, 4], 2)
get_random_values_with_default_attempts([1, 2, 3, 4], size=2)
get_random_values_with_default_attempts(choices=[1, 2, 3, 4], size=2)
get_random_values([1, 2, 3, 4])
get_random_values([1, 2, 3, 4], 3)
get_random_values([1, 2, 3, 4], size=1)


def copy_file(path1, path2):
    with open(path1, 'r') as f:
        data = f.read()
    with open(path2, 'w') as f:
        f.write(data)

copy_file('C:/Users/User/PycharmProjects/pythonProject2/result.txt', 'C:/Users/User/PycharmProjects/pythonProject2/result_copy.txt',)


def read_line_by_line(path):
    file = open(path, 'r')
    otvet = {}
    a = os.path.getsize(path)
    otvet['size'] = a
    b = 0
    dfs = {}
    for line in file:
        b += 1
        c = {k: v for k, v in Counter(line).items() if v > 1}
        dfs.update(c)
    s = (OrderedDict(sorted(dfs.items(), key=lambda t: t[1], reverse=True)))
    srez3 = list(s)[0:3]
    out = {}
    for key_srez in srez3:
        otvet[key_srez] = dfs.get(key_srez)

    otvet['count'] = b
    print('otvet', otvet)

    file.close()


read_line_by_line('C:/Users/User/Downloads/big.txt')


