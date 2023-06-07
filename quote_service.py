import wikiquote as wq
import random
from googletrans import Translator

def get_quote(word):
    """
    Retrieves a quote by searching for the given word (person's name) using the wikiquote library.

    Args:
        word (str): The word to search for.

    Returns:
        str: The retrieved quote or "Quote not found" if no quote is found.
    """
    try:
        search = wq.search(word)[0]
        quote = wq.quotes(search, lang="en")
        unchecked = random.choice(quote)
        final_step = translate(unchecked)
        return final_step
    except:
        return "Quote not found"

def get_random_quotes():
    """
    Retrieves the quote of the day using the wikiquote library.

    Returns:
        str: The quote of the day or "Quote not found" if no quote is found.
    """
    try:
        return wq.qotd()
    except:
        return "Quote not found"

def translate(sentence):
    """
    Translates the given sentence to English using the googletrans library.

    Args:
        sentence (str): The sentence to translate.

    Returns:
        str: The translated sentence or the original sentence if it's already in English.
    """
    translator = Translator()
    lang = translator.detect(sentence)
    if not lang == "en":
        return translator.translate(sentence, dest='en').text
    else:
        return sentence
