import timeit
import sys

def comprehensions(emails):
    return [mail for mail in emails if mail.endswith('@gmail.com')]

def loop_(emails):
    lst = []
    for mail in emails:
        if mail.endswith('@gmail.com'):
            lst.append(mail)
    return lst

def maps(emails):
    return list(map(lambda x: x.endswith('@gmail.com'), emails))

def filters(emails):
    return list(filter(lambda x: x.endswith('@gmail.com'), emails))


def main(args):
    try:
        arg = args[1].lower() 
        num = int(args[2])
        emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

        if arg == 'loop' and num > 0 : 
            res = timeit.timeit(f'loop_({emails})', setup='from __main__ import loop_', number=num)
        elif arg == 'map' and num > 0: 
            res = timeit.timeit(f'maps({emails})', setup='from __main__ import maps', number=num)
        elif arg == 'list_comprehension' and num > 0: 
            res = timeit.timeit(f'comprehensions({emails})', setup='from __main__ import comprehensions', number=num)
        elif arg == 'filter' and num > 0: 
            res = timeit.timeit(f'filters({emails})', setup='from __main__ import filters', number=num)
        print(res)
    except:
        print("Argument must be loop, map, filter or list_comprehension. Number must be positive.")

if __name__ == '__main__':
    if len(sys.argv) == 3:
            main(sys.argv)
    else:
        print("Use for example python3 benchmark.py filter 100")