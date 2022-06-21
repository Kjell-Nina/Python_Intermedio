my_list =  [1,2,3,4,5]
#abc=[i**2 for i in my_list]
## abc=[]
## for i in my_list:
##     i=i**2
##     print(i)
##     abc.append(i)
abc=list(map(lambda x: x**2, my_list)) #map mostrar todo lo que se genere
print(abc)