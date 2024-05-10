def translator(word):
    translations = {
        "hello": "hola",
        "goodbye": "adiós",
        "thank you": "gracias",
        "yes": "sí",
        "no": "no",
        "you're welcome": "de nada",
        "mom": "mama",
        "dad": "papa",
        "run": "correr",
        "walk": "caminar",
        "dog": "perro"
    }

    if word.lower() in translations:
        return translations[word.lower()]
    else:
        add_translation = input("Translation not found. Would you like to add the word? (yes/no): ")
        if add_translation.lower() == 'yes':
            new_translation = input("Enter the translation for '" + word + "': ")
            translations[word.lower()] = new_translation
            return "Translation added"
        else:
            return "Translation not found"


while True:
    word_to_translate = input("Enter a word to translate or type 'quit' to exit: ")
    if word_to_translate.lower() == 'quit':
        print("Exiting Translator")
        break
    else:
        print(translator(word_to_translate))
