"""print fibonnaci sequence"""


def fibonacci(n):
    f = [0, 1]
    if n == 0 or n == 1:
        return (f[n])
    for i in range(n):
        f.append(f[i] + f[i + 1])

    return f[n]


n = int(input())
print(fibonacci(n))