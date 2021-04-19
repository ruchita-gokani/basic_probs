# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc."

def alphabet_position(text):
    text_list = list(text)
    num_list = []
    for i in text_list:
        if i.isalpha():
            if i.isupper():
                i = i.lower()
                num_list.append(ord(i)-96)
            else:
                num_list.append(ord(i)-96)
        else:
            continue
    num_list = ' '.join(map(str, num_list))
    print(num_list)


def main():
    text_string = str(input("Enter a string. This function will return the alphabets of each letter in that string:\n"))
    return alphabet_position(text_string)


if __name__ == "__main__":
    main()
