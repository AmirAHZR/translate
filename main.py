from modes.developer.add_word.add_word import develop_add_word
from modes.user.search import *
from pyrobale import Client, Message
client = Client("1183714514:FSoo9j5jYUPlP5ESUqWRBWR0K9JfoRWiorc")

@client.on_command('translate')
async def get_word(m1:Message):
    

    result = user_mode(m1.text)
        
    if result[0]:
        m1.reply(f"{result[0]}")

client.run()
'''
else:
    adad = input("Sorry! We havent got this word in our dictionery.\nDo you want to add your word to our dictioniry? Y/N\n")
    if adad == "Y":
        res = develop_add_word(result[1], result[2], result[3])
        if res:
            print("Thank for helping us!")
        else:
            print("Thank! but we have that word in our dict!")




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

        

elif select == "3":
    print("Developers:\nAmir AHZ\nGithub: github.com/Amir-AHZR")
elif select == "4":
    break

        

'''