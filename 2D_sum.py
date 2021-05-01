"""Sum all values in a 2D array."""


def arr_sum(arr):
    result = 0
    for row in arr:
        for column in row:
            result += column
    return result


if __name__ == '__main__':
    array = [
        [-1,2,1],
        [2,-1],
        [1,2,-1],
        [0]
    ]
    print(arr_sum(array))
