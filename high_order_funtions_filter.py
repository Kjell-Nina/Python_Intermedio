my_list = [1,4,5,6,9,7,13,19,21]
# add= [ i for i in my_list if i%2 != 0]
# print(add)
odd=list(filter(lambda x : x%2 != 0, my_list))
print(odd)