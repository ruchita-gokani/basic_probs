"""Merging 2 Packages
Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.
Analyze the time and space complexities of your solution.
Example:
input: arr = [6, 4, 15, 16, 10], lim = 21 output: [3, 1] # since these are the indices of the # weights 6 and 15 whose sum equals to 21
Constraints:
[time limit] 5000ms
[input] array.integer arr
0 ≤ arr.length ≤ 100
[input] integer limit
[output] array.integer"""


def get_indices_of_item_weights(lim, arr):
    pos = {}
    N = len(arr)
    for i in range(N):
        if arr[i] in pos:
            return [i, pos[arr[i]]]
        else:
            c = lim - arr[i]
            pos[c] = i
    return []


if __name__ == '__main__':
    lim = 21
    arr = [4,5,1,9,10,15,6]
    print(get_indices_of_item_weights(lim, arr))
