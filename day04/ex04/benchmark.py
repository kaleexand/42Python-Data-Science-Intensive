import timeit
import sys
from collections import Counter
from random import randint

def my_fun(list_):
    dct = {}
    for el in list_:
        if el in dct:
            dct[el] += 1
        else:
            dct[el] = 1
    return dct

def add_count(list_):
    c = Counter()
    for i in list_:
        c[i] += 1
    # print(c)
    return c

def top_my_fun(list_):
    return dict(sorted(my_fun(list_).items(), key=lambda x: x[1], reverse=True)[:10])

def main():
    try:
        list_ = [randint(0, 100) for i in range(1000000)]
        num = 1
        add_count(list_)
        res_my = timeit.timeit(f'my_fun({list_})', setup='from __main__ import my_fun', number=num)
        res_cnt = timeit.timeit(f'add_count({list_})', setup='from __main__ import add_count', number=num)
        my_top = timeit.timeit(f'top_my_fun({list_})', setup='from __main__ import top_my_fun', number=num)
        cnt_top = timeit.timeit(f'add_count({list_}).most_common(10)', setup='from __main__ import add_count', number=num)
        # print(top_my_fun(list_))
        print(f'my function: {res_my} \nCounter: {res_cnt} \nmy top: {my_top} \nCounter\'s top: {cnt_top}')
    except:
        print("Error")

if __name__ == '__main__':
    main()