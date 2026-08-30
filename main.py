from modes.developer.add_word.add_word import develop_add_word
from modes.user.search import *
from batch import batch_translate
import tkinter as tk
from tkinter import filedialog
from balethon import Client
from balethon.objects import Message
from balethon.conditions import private, equals
import config

bot = Client(config.TOKEN)


while True:

    select = input(
        "please select your mode:\n"
        "1.Translate\n"
        "2.Developer mode\n"
        "3.Developers\n"
        "4.Batch Translate \n"   
        "5.Exit\n"
    )

    if select == "1":
        while True:
            result = user_mode()
            if result == "0":
                break
            if result[0]:
                print(result[0])
            else:
                adad = input(
                    "Sorry! We havent got this word in our dictionery.\n"
                    "Do you want to add your word to our dictioniry? Y/N\n"
                )
                if adad == "Y":
                    res = develop_add_word(result[1], result[2], result[3])
                    if res:
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
            res = develop_add_word(list_lang[origin_langs - 1], kalame, langs)
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
      


        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="select txt format file",
            filetypes=[("text file", "*.txt")], 
            defaultextension=".txt"
        )

        if file_path:

            if file_path.lower().endswith('.txt'):
                print(f"File selected correctly:{file_path}")
         
           

        
     
        batch_translate(file_path)

    elif select == "5":
        
        break
