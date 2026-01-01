def load_languages(list_of_langueges = list):
    for ind, obj in enumerate(list_of_langueges):
        print(f"{ind +1}.{obj}")
    origin_num = int(input())
    origin = list_of_langueges.pop(origin_num-1)
    for ind, obj in enumerate(list_of_langueges):
        print(f"{ind +1}.{obj}")
    destination = int(input())
    list_of_langueges.insert(origin_num-1,origin)
    return origin, destination

        


