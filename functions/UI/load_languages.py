def load_languages(list_of_langueges = list):
    for i in range(2):
        if i == 0:
            print("Please Enter the origin langueage")
        else:
            print("Please Enter the destination langueage")
        for index,origin in enumerate(list_of_langueges):
            print(f"{index}.{origin}")
        

