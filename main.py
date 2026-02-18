from modes.developer.add_word.add_word import develop_add_word
from modes.user.search import *

print(langs)
while True:
        select = input("please select your mode:\n1.Translate\n2.Developer mode\n3.Developers\n4.Help us\n5.Exit\n")
        if select == "1":
            while True:
                result = user_mode()
                if result == "0":
                    break
                if result[0]:
                    print(result[0])
                    add = input("This word mean another word?Y/N\n")
                    if add == "Y" or "y":
                        new_word = input("Enter your new word:\n")

                else:
                    adad = input("Sorry! We havent got this word in our dictionery.\nDo you want to add your word to our dictioniry? Y/N\n")
                    if adad == "Y":
                        res = develop_add_word(result[1], result[2], result[3])
                        if not(res):
                            print("Thank for helping us!")
                        else:
                            print("Thank! but we have that word in our dict!")
                breaks = input("Do you want to continue? Y/N\n")
                if breaks != "Y" or "y":
                    break


        elif select == "2":
            while True:

                print("Enter the origin langueges:")
                for index, item in enumerate(list_lang):
                    print(f"{index+1}-{item}")

                origin_langs = int(input())

                kalame = input("Please enter the word to check is it in our dict or no\n")
                res = develop_add_word(list_lang[origin_langs-1],kalame, langs )
                if res:
                    print("Thank for helping us!")
                else:
                    print("Thank! but we have that word in our dict")

                breaks = input("Do you want to continue? Y/N\n")
                if breaks != "Y" or "y":
                    break
        elif select == "3":
            print("Developers:\nAmir AHZ\nGithub: github.com/Amir-AHZR")
        elif select == "4":
            print("github.com/Amir-AHZR/translate   ")
        elif select == "5":
            break


