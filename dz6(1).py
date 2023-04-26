def summ_elem_list(a_list: list):
    result = 0

    for element in a_list:
        if type(element) is not list:
            result += element

        else:
            result += summ_elem_list(element)

    return result


print(summ_elem_list([]))
print(summ_elem_list([1, 2]))
print(summ_elem_list([1, [2, 3, [4], [5, 6, [7]]]]))


def copi_elem(a_list, d):
    result = []
    i = 0
    l = len(a_list)
    if d == 0:
        return result
    for el in range(d):
        j = el % l
        result.append(a_list[j])
    return result


print(copi_elem(['a', 'b', 'c'], 7))
print(copi_elem(['a', 'b', 'c'], 5))
print(copi_elem(['a', 'b', 'c'], 0))


import random
import string
import time

PASSWORD = ''.join(random.choices(string.ascii_letters, k=2))
print(PASSWORD)
def password_checker(password):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return


def password_cracker():
    password = ""
    while password != PASSWORD:
        password = ""
        while len(password) != len(PASSWORD):
            y = ''.join(random.choices(string.ascii_letters, k=4))
            start = time.time()
            password_checker(y)
            time.sleep(0.1)
            end = time.time()
            #print(end - start)
            password = str(password) + str(y)
        print(password)
    print("Password:", password)


password_cracker()