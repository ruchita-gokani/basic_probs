"""Find duplicate characters in a String and count the number of occurrences of the duplicate characters
"""


def char_duplicates(statement):
    d = {}
    a = []
    for i in statement:
        if i == ' ' or i == '.':
            continue
        if i.lower() in d:
            d[i] += 1
        else:
            d[i] = 0
    for k,v in d.items():
        if v > 1:
            print("Duplicate character {} appears {} times".format(k,str(v)))


if __name__ == '__main__':
    test_input = "Find the duplicates in this string. try as many as possible"
    char_duplicates(test_input)