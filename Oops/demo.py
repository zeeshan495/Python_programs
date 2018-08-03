
language = {}
language["java1"] = {
    "framework": "spring",
    "source": "open"
}
language["python2"] = {
    "framework": "django",
    "source": "open"
}




import json
# from JsonFiles import *
class Demo:
    # data = json.load(open("DataManagment.json","r"))
    # data["Inventory1"]["price"] = 30
    # print(data)

    # with open("DataManagment.json", "w") as abc:
    #     json.dump(data,abc)
    # f = open("demoJson.json","w")
    data = json.dumps(language)
    print(data)
    # print(data)
    # f = open("demoJson.json","w")
    # f.write(data)

    with open("/home/bridgeit/Zeeshan_Python/JsonFiles/demoJson.json",'w') as f:
        f.write(data)

    # main_list = {}
    # my_list = {}
    # my_list["info1"] = {123}
    # my_list["info2"] = {456}
    # my_list["info3"] = {789}
    # main_list["mainInfo"] = my_list
    # print(type(main_list))
    # print(main_list)
