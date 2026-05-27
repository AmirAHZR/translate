import pickle

langs = {
    "Farsi" : [],
    "English" : [],
    }
list_lang = list(langs.keys())
for i in list_lang:
    with open(f'document\words_pkl\{i}.pkl', 'rb') as f:   # rb = read binary
        loaded_list = pickle.load(f)
        langs[i] = loaded_list


