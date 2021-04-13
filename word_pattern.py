"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


def word_pattern(pattern, s):
    s_list = s.split(' ')
    p_dict = {}
    s_dict = {}
    if len(pattern) != len(s_list):
        return False
    for i in range(len(pattern)):
        try:
            p_dict[pattern[i]] = p_dict[pattern[i]] + [(s_list[i])]
        except KeyError:
            p_dict[pattern[i]] = [s_list[i]]
    for i in range(len(s_list)):
        try:
            s_dict[s_list[i]] = s_dict[s_list[i]] + [(pattern[i])]
        except KeyError:
            s_dict[s_list[i]] = [pattern[i]]

    for value in p_dict.values():
        if len(set(value)) != 1:
            return False
    for value in s_dict.values():
        if len(set(value)) != 1:
            return False
    return True


if __name__ == '__main__':
    input_pattern = input("Enter test pattern: ")
    input_string = input("Enter test string: ")
    if word_pattern(input_pattern, input_string):
        print("Pattern matches string")
    else:
        print("Pattern does not match")
