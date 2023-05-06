# 1).

from collections import Counter

nums = [2, 3, 3, 3]


def nums_func():
    num_counts = Counter(nums)
    min_num = min(num_counts, key=num_counts.get)
    return min_num


print(nums_func())

# 2).

number = [9, 9, 9, 9]
number_new = []


def spisok_func():
    result = int("".join(map(str, number))) + 1

    for i in str(result):
        i = int(result % 10)
        number_new.append(i)
        result = result / 10
    return number_new[::-1]


print(spisok_func())

# 3).

import string


def string_func(string_new):
    string_new = string_new.lower()
    translator = str.maketrans('', '', string.punctuation)
    string_new = string_new.translate(translator)
    string_new = string_new.replace(" ", "")
    if string_new == string_new[::-1]:
        return True
    else:
        return False


string_new = "A man,a plan,a canal:Panama"
print(string_func(string_new))
