def run():
    my_list=[1,"Hello",True,4.5]
    my_dicc={"firstname":"Kjell" ,"lastname":"Nina"}

    super_list= [
        {"firstname":"Antony" ,"lastname":"Aguilar"},
        {"firstname":"Matias" ,"lastname":"Gomez"},
        {"firstname":"Jacoba" ,"lastname":"Cahuana"},
        {"firstname":"Edurne" ,"lastname":"Moar"}     
    ]
    super_dicc={
        "natural_nums":[1.2,3,4,5],
        "integer_nums":[-2,-1,0,1,2],
        "floating_nums":[1.1,5.68,4.87]
    }

    # for key , value in super_dicc.items():
    #     print(key,"-", value)
    for i in super_list:
        print(i["firstname"], " - ",i["lastname"])


if __name__=="__main__":
    run()