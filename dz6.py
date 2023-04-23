def summ_elem_list(a_list: list, d: int = -1):
    result = []

    for element in a_list:
        if d == 0 or type(element) is not list:
            result.append(element)

        else:
            result.extend(summ_elem_list(element, d - 1))

    return result


print(sum(summ_elem_list([])))
print(sum(summ_elem_list([1, 2])))
print(sum(summ_elem_list([1, [2, 3, [4], [5, 6, [7]]]])))


def copi_elem(a_list: list, d: int):
    result = []
    i = 0
    s = len(a_list)
    if d == 0:
        return result

    while True:

        for el in a_list:
            i += 1
            result.extend(el)
            if i >= d:
                return result
    print(result)


print(copi_elem(['a', 'b', 'c'], 7))
print(copi_elem(['a', 'b', 'c'], 5))
print(copi_elem(['a', 'b', 'c'], 0))


import random
import string
import time


def password_checker(password):
    PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))
    time.sleep(0.1)
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return password_checker(password)
        return password


password_checker('hjju')