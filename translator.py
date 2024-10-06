#!/usr/bin/env python3

from deep_translator import GoogleTranslator
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

### Pulls down language list from Google
language_list = GoogleTranslator().get_supported_languages() 

### Creates word completer menu
def menu():
    completer = WordCompleter(language_list, ignore_case=True)
    global language
    language = prompt("Choose the language you want to translate to: ", completer=completer)
    if language:
        print(f"You selected: {language}")
    else:
        menu()
menu()

def english_to_spanish(text):
    translator = GoogleTranslator(source='auto', target=language)
    return translator.translate(text)

text_to_translate = input("What is the English word you would like to translate?:  ")
translated_text = english_to_spanish(text_to_translate)

print("Translated Word: " + '\033[1m' + translated_text)
