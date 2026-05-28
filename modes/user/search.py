import functions.UI.load_languages
from document.languages_words import langs, list_lang
from functions.filtering.word_filtering import filtering
from functions.translate.translate import *
def user_mode(word):
    origin, destination = functions.UI.load_languages.load_languages(list_lang)


    
    
    result = translate(filtering(word), langs[origin], langs[destination])
    return result, origin, word, langs