from functools import reduce
 
my_list=[2,2,2,2,2]
# all_mult = 1

# for i in my_list:
#     all_mult=all_mult*i
# print(all_mult)
all_mult=reduce(lambda a,b:a*b, my_list) #a seria el 1er 2,b el 2do 2, despues el resultado es a y el 3er elemeto es b
print(all_mult)