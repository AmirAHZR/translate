
def load_languages(list_of_langueges = list):

    print("Please choose the origin language:")
    for index, object in enumerate(list_of_langueges):
        print(f"{index +1}-{object}")
    origin_num = int(input())
    origin = list_of_langueges.pop(origin_num-1)
    
    if len(list_of_langueges)+1!=2:
        print("Please choose the destination language:")
        for ind, obj in enumerate(list_of_langueges):
            print(f"{ind +1}-{obj}")
        destination_num = int(input())
        destination = list_of_langueges[destination_num-1]
        
        
    else:

        destination = list_of_langueges[0]
        print(f"{destination} Atuo selecting :)")

    list_of_langueges.insert(origin_num-1, origin)


    return origin, destination