
def add_word(origin_lang, main_word, langs_dict = dict):
    helper = int()
    if not(main_word in langs_dict[origin_lang]):
        langs_dict[origin_lang].append(main_word)
        helper += 1
    index = langs_dict[origin_lang].index(main_word)
    for i in list(langs_dict.keys()):
        if i != origin_lang :
            try:
                if not(langs_dict[i][index]):
                    print(f"please enter a instead of {main_word} in {i}")
                    print("if you dont know please do not enter anything(just enter)")
                    new_word = input()
                    langs_dict[i].remove(langs_dict[i][index])
                    langs_dict[i].insert(index ,new_word)
                    helper +=1
            except:      
                print(f"please enter a instead of {main_word} in {i}")
                print("if you dont know please do not enter anything(just enter)")
                new_word = input()
                langs_dict[i].append(new_word)
                helper += 1

    return helper