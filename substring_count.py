"""Write a function to count how many times the substring appears in the larger String."""


def count_sub_string(s, sub):
    count = 0
    n = len(sub)+1
    for i in range(len(s)):
        if s[i] == sub[0] and sub in s[i:i+n]:
            count +=1

    return count


if __name__ == '__main__':
    test = ""
    sub_string = 't'
    print(count_sub_string(test, sub_string))
