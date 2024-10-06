#!/usr/bin/env python3

from deep_translator import GoogleTranslator
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def startup_menu():
    print("")
    print("======================================")
    print("    The Josh and Carter Translator    ")
    print("======================================")
    print("")

def get_supported_languages():
    return GoogleTranslator().get_supported_languages()

def select_language(language_list):
    completer = WordCompleter(language_list, ignore_case=True)
    language = prompt("Choose the language you want to translate to: ", completer=completer)
    if language:
        print(f"You selected: {language}")
        return language
    else:
        return select_language(language_list)

def translate_it(text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)
    return translator.translate(text)

def main():
    startup_menu()
    language_list = get_supported_languages()
    language = select_language(language_list)
    text_to_translate = input("What would you like to translate?:  ")
    translated_text = translate_it(text_to_translate, language)
    print("")
    rerun()

def rerun():
    rerun_choice = input("Would you like to translate more? (Y/N):  ").lower()
    if rerun_choice in ["y", "yes"]:
        main()
    else:
        pass

if __name__ == "__main__":
    main()
