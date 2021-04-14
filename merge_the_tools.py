"""https://www.hackerrank.com/challenges/merge-the-tools/problem
Consider the following:

A string, s , of length n where s = c0c1c2c2....cn.
An integer,k , where k is a factor of n.
We can split s into n/k substrings where each substring,ti , consists of a contiguous block of k characters in s.
Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once.
In other words, if the character at some index j in ti occurs at a previous index <j in ti,
then do not include the character in string ui.

1. go through the string and divide it in x strings of length k
2. store new string  in form of set and remove duplicates
3. convert set into string and print
"""


def merge_the_tools(string, k):#"AABCAAADA" "3" [AAB][CAA]{ADA]
    N = len(string)
    num_of_strings = int(N/k)

    # for i in range(num_of_strings):
    #     t = ''
    #     t = t + string[k*i:k*(i+1)]
    #     u = {}
    #     count = 0
    #     for j in t:
    #         if j in u:
    #             u[j] += 1
    #         else:
    #             u[j] = count+1
    #     print(''.join(u.keys()))
    for i in range(num_of_strings):
        u = ''
        for j in range(k):
            if string[j + k*i] not in u:
                u += string[j+k*i]
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
