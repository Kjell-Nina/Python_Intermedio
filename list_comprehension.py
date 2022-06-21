def run():
    #list= []
    # for i in range (1,101):
    #     if i % 3 !=0:
    #         list.append(i)
    # print(list)
    list = [i**2 for i in range(1,101) if i % 3 != 0]
    print(list)
           # element for element in iterable if condition


if __name__ == "__main__":
    run()