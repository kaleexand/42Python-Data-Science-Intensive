import sys
import psutil

def ordinary(path):
    with open(path, 'r') as f:
        list_ = f.readlines()
    return list_


def main():
    if len(sys.argv) == 2:
        try:
            for line in ordinary(sys.argv[1]):
                pass
            process = psutil.Process()
            gb = 2**30
            mem = process.memory_info().rss / gb
            cpu = process.cpu_times()
            print(f'Peak Memory Usage = {mem:.3f} Gb')
            print(f'User Time + System Time = {cpu.user + cpu.system:.2f} s')
        except:
            print("Error")
    else:
        print(f'Use python3 ordinary.py ratings.csv')


if __name__ == '__main__':
    main()