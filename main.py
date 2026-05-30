from modes.developer.add_word.add_word import develop_add_word
from modes.user.search import *
from functions.UI.load_languages import load_languages

def batch_translate(filepath):
    """
    Reads every line of a text file and tries to translate it.
    Results are saved to  <original_filename>_translated.txt
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
        return

    if not words:
        print("The file is empty.")
        return

    output_path = filepath.rsplit(".", 1)[0] + "_translated.txt"
    found = 0
    not_found = []
    la = load_languages(list_lang)
    with open(output_path, "w", encoding="utf-8") as out:
        for word in words:
            
            result = translate(word.strip(), langs[la[0]], langs[la[1]])  
            
            if result and result[0]:
                out.write(f"{word}  -->  {result}\n")
                found += 1
            else:
                out.write(f"{word}  -->  [NOT FOUND]\n")
                not_found.append(word)

    print(f"\nDone! {found}/{len(words)} words translated.")
    print(f"Output saved to: {output_path}")

    



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

    elif select == "3":
        print("Developers:\nAmir AHZ\nGithub: github.com/Amir-AHZR")

    elif select == "4":
      
        filepath = input("Enter the path to your text file (one word per line):\n").strip()

        
     
        batch_translate(filepath)

    elif select == "5":
        
        break
