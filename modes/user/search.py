import functions.UI.load_languages
from document.languages_words import langs, list_lang
from functions.filtering.word_filtering import filtering
from functions.translate.translate import *
def user_mode():
    origin, des = functions.UI.load_languages.load_languages(list(list_lang))
    
    word = input()

    result = translate(filtering(word), langs[list_lang[origin]], langs[list_lang[des]])
    return result, origin, word