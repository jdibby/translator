#!/usr/bin/env python3

from deep_translator import GoogleTranslator
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def get_supported_languages():
    """ Grab the list of supported languages from Google """
    return GoogleTranslator().get_supported_languages()

def startup_menu():
    """ Display a startup menu """
    print("")
    print("======================================")
    print("         The Translator    ")
    print("======================================")
    print("")

def select_language(language_list):
    """ Show the user a menu for languages """
    completer = WordCompleter(language_list, ignore_case=True)
    language = prompt("Choose the language you want to translate to: ", completer=completer)
    if language:
        print(f"You selected: {language}")
        return language
    else:
        return select_language(language_list)  # If there is no language selected, do it again

def translate_it(text, target_language):
    """ Translate the text into the language selected """
    translator = GoogleTranslator(source='auto', target=target_language)
    return translator.translate(text)

def get_text_to_translate():
    """ Prompt the user asking what to translate """
    return input("What would you like to translate?: ")

def rerun():
    """ Function to potentially rerun all of this over again """
    rerun_choice = input("Would you like to translate more? (Y/N):  ").lower()
    if rerun_choice in ["y", "yes"]:
        main()
    else:
        pass

def main():
    """ Run the translator """
    startup_menu()
    language_list = get_supported_languages()
    selected_language = select_language(language_list)
    text_to_translate = get_text_to_translate()
    translated_text = translate_it(text_to_translate, selected_language)
    print("Translated Text: " + translated_text) 
    print("")
    rerun()

if __name__ == "__main__":
    main()
