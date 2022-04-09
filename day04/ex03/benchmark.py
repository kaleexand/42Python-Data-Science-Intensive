import timeit
import sys
from functools import reduce

def reduce_(num_sq):
    l = [i for i in range(1, num_sq + 1)]
    # print(reduce(lambda sum_, i: sum_ + i**2, l))
    return reduce(lambda sum_, i: sum_ + i**2, l)

def loop_(num_sq):
    sum_ = 0
    l = [i for i in range(1, num_sq + 1)]
    for i in l:
        sum_ += i**2
    # print(sum_)
    return sum_

def main(args):
    try:
        arg = args[1].lower() 
        num = int(args[2])
        num_sq = int(args[3])

        l = [i for i in range(1, num_sq + 1)]

        if arg == 'loop' and num > 0 and num_sq > 0: 
            res = timeit.timeit(f'loop_({num_sq})', setup='from __main__ import loop_', number=num)
        elif arg == 'reduce' and num > 0 and num_sq > 0:
            res = timeit.timeit(f'reduce_({num_sq})', setup='from __main__ import reduce_', number=num)
        print(res)
    except:
        print("Argument must be loop or reduce. Number must be positive.")

if __name__ == '__main__':
    if len(sys.argv) == 4:
            main(sys.argv)
    else:
        print("Use python3 benchmark.py loop 100")