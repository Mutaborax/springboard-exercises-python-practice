def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # Split the phrase into a list of words
    words = phrase.split()

    # Iterate over each word in the list
    for i in range(len(words)):

        # Capitalize the first letter of the word and add the rest of the word
        words[i] = words[i][0].upper() + words[i][1:].lower()

    # Join the words back together into a string with spaces in between
    return ' '.join(words)
