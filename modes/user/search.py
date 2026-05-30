import functions.UI.load_languages
from document.languages_words import langs, list_lang
from functions.filtering.word_filtering import filtering
from functions.translate.translate import *
from pyrobale import Message, UpdatesTypes, InlineKeyboardButton, InlineKeyboardMarkup, CopyTextButton, Client
def search():
    client = Client("1183714514:FSoo9j5jYUPlP5ESUqWRBWR0K9JfoRWiorc")
    @client.on_command("translate")
    async def origin(cmd:Message):
        
        buttons = InlineKeyboardMarkup()
        for orig in list_lang:
            buttons.add_button(f"{orig}", copy_text_button=CopyTextButton(f"{orig}"))
            buttons.add_row()
        
        await cmd.reply("Choose the origin language\n(Click on it, then paste it on keyboard)", reply_markup=buttons)
        @client.on_message()
        async def orgi(org:Message):
            print(list_lang)
            print(org, list_lang)
            buttons2 = InlineKeyboardMarkup()
            orig_num = list_lang.index(org.text)
            list_lang.pop(orig_num)
            for des in list_lang:
                buttons2.add_button(f"{des}", copy_text_button=CopyTextButton(f"{des}"))
                buttons2.add_row()
            
            await org.reply("Choose the des language\n(Click on it, then paste it on keyboard)", reply_markup=buttons)
            @client.on_message()
            async def desi(des:Message):
                list_lang.insert(orig_num, org.text)
                await des.reply("Enter the word", reply_markup=buttons)
                @client.on_message()
                async def wordi(word:Message):
                    res = translate(word.text, org.text, des.text)
                    print(res)
                    
    client.run() 

