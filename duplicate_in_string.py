"""Describe and code an algorithm that returns the first duplicate character in a string?"""

"""
1. take a string input from the user
2. pass that string into a function
3. create a function to go through the characters in a string 
4. add new string characters as keys to dictionary
5. if the character is present in the dictionary, increment the count and exit the dictionary
"""


def duplicate_char(problem_string):
    characters_dict = dict()
    count = 0

    for character in problem_string:
        if character not in characters_dict.keys():
            characters_dict[character] = count + 1
        else:
            characters_dict[character] += 1
            break
    if characters_dict[character] == 2:
        duplicate_message = "First duplicate character is {}".format(character)
        return duplicate_message
    else:
        return "No duplicates found"


if __name__ == '__main__':
    string = input('Enter a random string of characters to get the first duplicate: ')
    print duplicate_char(string)
