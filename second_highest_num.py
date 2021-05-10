"""Find the second highest number in a given array. If no second highest number present, return 0"""


def second_highest(arr):
    large = 0
    second_large = 0
    for i in arr:
        if i > large:
            second_large = large
            large = i
        elif second_large < i < large:
            second_large = i

    return second_large


if __name__ == '__main__':
    num = [100,97,95,97,33,42,100,-1,-100]
    print(second_highest(num))
