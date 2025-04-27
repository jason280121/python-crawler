

# list for loop
list1 = ['apple', 'cat', 'dog']
# apple cat dog
# for list1 in list1:
#     print(list1)

# tuple for loop
t1 = ('apple', 'cat', 'dog')
# apple cat dog
# for tup01 in t1:
#     print(f'{tup01}')

# set for loop
# s1 = {'apple', 'cat', 'dog'}
# apple cat dog
# for set01 in s1:
#     print(set01)


# for loop range(0-9)
# for item in range(0, 10):
#     print(item)

# list[] for loop range(len)
# 0,1,2
# apple, cat, dog
for item in range(len(list1)):
    print(item, end=', ')
    print(list1[item], end=', ')


# tuple() for loop range(len)
# 0,1,2
# apple, cat, dog
for item in range(len(t1)):
print(item, end=', ')
print(t1[item], end=', ')

# set{} for loop range(len)
# 0,1,2
# apple, cat, dog
# for item in range(len(s1)):
#     # print(item)
#     print(s1[item])
