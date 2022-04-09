import timeit

def comprehensions(emails):
    return [mail for mail in emails if mail.endswith('@gmail.com')]

def loop_(emails):
    lst = []
    for mail in emails:
        if mail.endswith('@gmail.com'):
            lst.append(mail)
    return lst

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

    loop_t = timeit.timeit(f'loop_({emails})', setup='from __main__ import loop_', number=9000000)
    comp = timeit.timeit(f'comprehensions({emails})', setup='from __main__ import comprehensions', number=90000000)

    if loop_t < comp:
        print('it is better to use a loop\n', str(loop_t) + 'vs' + str(comp))
    else:
        print('it is better to use a list comprehension\n', str(comp) + ' vs ' + str(loop_t), sep = '')

if __name__ == '__main__':
    main()