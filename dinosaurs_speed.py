"""
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)
Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from
fastest to slowest.
Do not print any other information.
'''
1. read from 2 csv files
2. create dictionaries of name: leglength, stridelength, stance and diet
3. for each name, calculate speed and store it in a new dictionary
4. parse dictionary for stance and create a new dictionary of all the bipedal dinos
    5. create list from dictionary
'''
"""
from math import sqrt
from collections import OrderedDict

speed_dict = dict()
g = 9.8
dataset_info = dict()
with open('usage_files/dataset1.csv', 'r') as dataset1:
    next(dataset1)
    for line in dataset1:
        name = line.split(',')[0]
        leg_length = line.split(',')[1]
        dataset_info[name] = leg_length

with open('usage_files/dataset2.csv', 'r') as dataset2:
    next(dataset2)
    for line in dataset2:
        stance = line.split(',')[2]
        if stance == "bipedal" or stance == "bipedal\n":
            stride_length = line.split(',')[1]
            name = line.split(',')[0]
            try:
                dataset_info[name] = [dataset_info[name], stride_length]
            except KeyError:
                dataset_info = dataset_info

for key, value in dataset_info.items():
    if len(value) == 2:
        speed_dict[key] = ((float(value[1]) / float(value[0])) - 1) * sqrt(float(value[0]) * float(g))

speed_sort = OrderedDict(sorted(speed_dict.items(), key=lambda x: x[1], reverse=True))

for k, v in speed_sort.items():
    print(k)

# with open('dataset2.csv', 'r') as csv_file2:
#     dataset_2 = csv.DictReader(csv_file2)
#     for info2 in dataset_2:
#         if info['NAME'] == info2['NAME'] and info2['STANCE'] == 'bipedal':
#             speed_dict[info['NAME']] = ((float(info2['STRIDE_LENGTH']) / float(info['LEG_LENGTH'])) - 1) * \
#                                  sqrt(float(info['LEG_LENGTH'])*float(g))
#
# speed_sort = OrderedDict(sorted(speed_dict.items(), key=lambda x: x[1], reverse=True))
# print(speed_sort.keys())
# for k, v in speed_sort.items():
#    print(k)
