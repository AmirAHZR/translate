from functions.add.add_word import add_word
from document.words_pkl.saver import saver
from document.languages_words import  list_lang

def develop_add_word(origin,word, langs):

    add_word(origin, word, langs)


    ind = 0
    for i in range(len(list_lang)):
        x = list_lang[ind]
    
        saver(f"document\words_pkl\{x}.pkl",langs[x])
        ind += 1
    return add_word(origin, word, langs)

