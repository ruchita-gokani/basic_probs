"""Write code that will accept two strings and return true if they are anagrams."""


def check_anagram(user_string1, user_string2):
    my_list1 = []
    my_list2 = []
    for i in range(len(user_string1)):
        if user_string1[i] == ' ':
            pass
        else:
            my_list1.append(user_string1[i].lower())
    for i in range(len(user_string2)):
        if user_string2[i] == ' ':
            pass
        else:
            my_list2.append(user_string2[i].lower())

    if len(my_list2) != len(my_list1):
        return "Strings are not anagrams"
    else:
        for i in range(len(my_list1)):
            if my_list1[i] not in my_list2:
                return "Strings are not anagrams"
            elif my_list1[i] in my_list2:
                my_list2.remove(my_list1[i])
                if not my_list2:
                    return "Strings are anagrams"


if __name__ == '__main__':
    test_string1 = input("Enter string1 for the test: ")
    test_string2 = input("Enter string2 for the test: ")
    print(check_anagram(test_string1, test_string2))