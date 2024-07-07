# translate_text.py

from googletrans import Translator

def translate_text(text, src='en', dest='kn'):
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

def write_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
