"""In a given sorted array of integers remove all the duplicates"""

int_list = [1, 1, 2, 3, 5, 8, 8]
new_list = []
for i in range(len(int_list)):
    if int_list[i] not in new_list:
        new_list.append(int_list[i])

print("change with new list ",  new_list)

for i in range(len(int_list)):
    try:
        if int_list[i] == int_list[i+1]:
            int_list.remove(int_list[i])
    except IndexError:
        break
print("Change with the same list ", int_list)