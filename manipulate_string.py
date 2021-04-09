"""Write a program takes in a string and a delimiter, and uses that delimiter to split a string
and then will reverse the characters in every word (or jumble of characters between the delimiters),
stuffing them back into a string when finished. ('The dog walks' becomes..... 'ehT god sklaw')"""


def reverse_string(test_string, delimiter):
    test_list = test_string.split(delimiter)
    jumbled_list = []
    for word in test_list:
        new_word = ''
        for i in range(len(word)):
            new_word = new_word + word[len(word)-1-i]
        jumbled_list.append(new_word)

    return delimiter.join(jumbled_list)


if __name__ == '__main__':
    sentence = input("Enter a sentence for the test: ")
    special_char = input('enter a delimiter to split the sentence: ')
    print(reverse_string(sentence, special_char))
