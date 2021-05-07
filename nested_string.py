"""Given a string S consisting of N characters. All characters are either open or close parentheses. Check if the string
is properly nested.
"""


def is_valid_pair(left, right):
    if left == '(' and right == ')':
        return True
    if left == '{' and right == '}':
        return True
    if left == '[' and right == ']':
        return True
    else:
        return False


def check_nesting(statement):
    stack = []
    for s in statement:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        else:
            if len(stack)==0:
                return 0
            last = stack.pop()
            if not is_valid_pair(last, s):
                return 0
    if len(stack) != 0:
        return 0
    return 1


if __name__ == '__main__':
    test = "[(])"
    if check_nesting(test) == 1:
        print("This is a valid nested string")
    else:
        print("The string is not properly nested")