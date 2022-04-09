import sys
import psutil

def generator(path):
    for line in open(path):
        yield line

def main():
    if len(sys.argv) == 2:
        try:
            for line in generator(sys.argv[1]):
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

# Yield это ключевое слово, которое используется примерно 
# как return — отличие в том, что функция вернёт генератор.