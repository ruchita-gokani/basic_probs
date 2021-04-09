"""Given a string, how would you determine if that string contains a palindrome?"""


def palindrome_string(test_string):
    test_list = test_string.split(' ')
    for word in test_list:
        new_word = ''
        for i in range(len(word)):
            new_word = new_word + word[len(word)-1-i]
        if new_word == word:
            return "string contains palindrome"


if __name__ == '__main__':
    sentence = input("Enter a sentence for testing the code: ")
    print(palindrome_string(sentence))
