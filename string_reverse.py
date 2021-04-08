"""Given a string (understood to be a sentence), reverse the order of the words. "Hello world" becomes "world Hello"""

test_string = "This is a string of off words"
test_list = test_string.split(' ')
new_string = ""

for i in range(0, len(test_list)):

    new_string = new_string + ' ' + test_list[len(test_list)-1 - i]
print(new_string)
