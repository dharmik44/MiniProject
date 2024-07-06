from googletrans import Translator

def translate_text(text, src='en', dest='kn'):
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

def write_to_file(translated_text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

