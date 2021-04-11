"""Given a string, how would you determine if that string contains a palindrome?"""


def palindrome_string(test_string):
    test_list = test_string.split(' ')
    for word in test_list:
        # if word == word[::-1]:
        #     return True
        new_word = ''
        n = len(word)
        for i in range(n):
            new_word = new_word + word[n-1-i]

        if new_word == word:
            return "string contains palindrome"


if __name__ == '__main__':
    sentence = input("Enter a sentence for testing the code: ")
    if palindrome_string(sentence):
        print("String has a palindrome")
    else:
        print("String does not have a palindrome")
