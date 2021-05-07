"""Create a function that takes two parameters; an array of integers and an integer. Your function should print the pair
numbers from the array that add up to the integer parameter.
"""


def int_sum(arr, num):
    diff = {}
    pairs = []
    for i in arr:
        d = num - i
        if d in diff:
            pairs.append([d, i])
        else:
            diff[i] = d
    return pairs


if __name__ == '__main__':
    a = [1,1,4,1,2,1,4]
    s = 5
    print(int_sum(a,s))
