"""Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,S .
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.
https://www.hackerrank.com/challenges/the-minion-game/problem"""


def minion_game(string): #BANANA
    k = 0
    s = 0
    N = len(string) #6

    vowels = "AEIOU"
    for i in range(N):
        if string[i] in vowels:
            k += (N-i)
        else:
            s += (N-i)
    if k > s:
        print("Kevin", k)
    elif s > k:
        print("Stuart", s)
    else:
        print("Draw")
    return


if __name__ == '__main__':
    s = input()
    minion_game(s)

