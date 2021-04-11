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
    pattern_list = list(pattern)  # ['a', 'b', 'b', 'a']
    s_list = s.split(' ')  # ['dog', 'cat', 'cat', 'dog']
    word_dict = {}
    if len(pattern_list) != len(s_list):
        return False
    else:
        for i in range(len(pattern_list)):
            try:
                word_dict[pattern_list[i]] = word_dict[pattern_list[i]] + [(s_list[i])]
            except KeyError:
                word_dict[pattern_list[i]] = [s_list[i]]

        for key, value in word_dict.items():
            if len(set(value)) != 1:
                return False
            else:
                continue
        return True


if __name__ == '__main__':
    input_pattern = input("Enter test pattern: ")
    input_string = input("Enter test string: ")
    if word_pattern(input_pattern, input_string):
        print("Pattern matches string")
    else:
        print("Pattern does not match string")