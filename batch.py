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

    


