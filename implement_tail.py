"""'''
implement tail

tail <filename> prints only the last 10 lines of the File
tail -n 20 <filename> reads last 20 lines from filename and writes to stdout
"""


def tail(filename, l, n=None):
    with open(filename, 'r') as f:
        if not n:
            x = int(l)-5
        else:
            x = int(l)-int(n)
        while x:
            next(f)
            x -= 1

        print(f.read())


tail('vm_stat.log', 8, n=2)
