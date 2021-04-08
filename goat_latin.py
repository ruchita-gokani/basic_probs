"""Goat Latin is a made-up language based off of English, sort of like Pig Latin.
The rules of Goat Latin are as follows:
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add 'ma'.
For example, the word 'goat' becomes 'oatgma'.If a word begins with a vowel (a, e, i, o, or u),
append 'ma' to the end of the word. For example, the word 'I' becomes 'Ima'.
Add one letter "a" to the end of each word per its word index in the  sentence, starting with 1.
That is, the first word gets "a" added to the end, the second word gets "aa" added to the end,
the third word in the sentence gets "aaa" added to the end, and so on.
Write a function that, given a string of words making up one sentence, returns that sentence in Goat Latin.
For example: string_to_goat_latin('I speak Goat Latin') would return: 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
"""


def convert_to_goat(test_string):
    if len(test_string) == 0:
        return None
    my_list = test_string.split(' ')
    vowels = ('a', 'e', 'i', 'o', 'u') # make it a tuple
    additional_string = 'a'
    new_list = []
    for index, word in enumerate(my_list):
        if word[0].lower() in vowels:
            word = word +'ma' + (additional_string*(index+1))
            new_list.append(word)
        else:
            word = word[1:]+word[0] + 'ma' + (additional_string*(index+1))
            new_list.append(word)

    return ' '.join(new_list)


if __name__ == '__main__':
    print(convert_to_goat("I speak Goat Latin"))