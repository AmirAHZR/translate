from pickle import dump

def saver(file_location, my_list = list):
    with open(file_location, 'wb') as f:    
        dump(my_list, f)


