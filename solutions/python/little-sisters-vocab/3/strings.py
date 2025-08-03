"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    '''

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    '''
    return f"un{word}"

def make_word_groups(vocab_words):
    '''

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    '''
    return f" :: {vocab_words[0]}".join(vocab_words)

def remove_suffix_ness(word):
    '''

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    '''
    
    without_suffix = word.split("ness")[0]
    return without_suffix[:-1] + "y" if without_suffix[-1] == "i" else without_suffix

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    return sentence.replace(".", "").split()[index] + "en"
