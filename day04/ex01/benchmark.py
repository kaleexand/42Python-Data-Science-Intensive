import timeit

def comprehensions(emails):
    return [mail for mail in emails if mail.endswith('@gmail.com')]

def loop_(emails):
    lst = []
    for mail in emails:
        if mail.endswith('@gmail.com'):
            lst.append(mail)
    return lst

def maps(emails):
    return list(map(lambda mail: mail if mail.endswith('@gmail.com') else None, emails))

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

    loop_t = timeit.timeit(f'loop_({emails})', setup='from __main__ import loop_', number=900000)
    maps_t = timeit.timeit(f'maps({emails})', setup='from __main__ import maps', number=900000)
    comp = timeit.timeit(f'comprehensions({emails})', setup='from __main__ import comprehensions', number=900000)

    time = sorted([loop_t, maps_t, comp])
    if loop_t < comp and loop_t < maps_t:
        print('it is better to use a loop\n', str(time[0]) + ' vs ' + str(time[1]) + ' vs ' + str(time[2]), sep='')
    elif comp < loop_t and comp < maps_t:
        print('it is better to use a list comprehension\n', str(time[0]) + ' vs ' + str(time[1]) + ' vs ' + str(time[2]), sep='')
    else:
        print('it is better to use a map\n', str(time[0]) + ' vs ' + str(time[1]) + ' vs ' + str(time[2]), sep='')

if __name__ == '__main__':
    main()