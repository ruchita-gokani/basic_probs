"""https://www.hackerrank.com/challenges/no-idea/problem"""


def no_idea(ar, a, b):
    h = 0
    for i in range(len(ar)):
        if ar[i] in a:
            h+=1
        if ar[i] in b:
            h-=1
    return h


if __name__ == '__main__':
    n,m = input().split(' ')
    arr = input().split(' ')
    a = set(input().split(' '))
    b = set(input().split(' '))
    print(no_idea(arr,a,b))