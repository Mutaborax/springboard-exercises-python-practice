def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    if len(phrase) == 0:
        return ""
    else:
        first_word = phrase.split()[0]
        return first_word.capitalize() + phrase[len(first_word):]
