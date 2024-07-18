import googletrans as trans
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translation = {}
print(trans.LANGUAGES)
translator = trans.Translator()

for word in french_words:
   word_fr = translator.translate(word,src='fr' ,dest='en')
   translation[word] = word_fr.text # type: ignore
