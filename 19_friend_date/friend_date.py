def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    a_hobbies = set(a[2])  # Convert hobbies to a set for efficient comparison
    b_hobbies = set(b[2])

    # Check if the intersection of the two sets of hobbies is non-empty
    if a_hobbies.intersection(b_hobbies):
        return True
    else:
        return False
