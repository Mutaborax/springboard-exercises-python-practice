def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    # Convert both numbers to strings
    num1_str = str(num1)
    num2_str = str(num2)

    # Get frequency of digits in both numbers using a dictionary
    freq1 = {}
    freq2 = {}

    for digit in num1_str:
        freq1[digit] = freq1.get(digit, 0) + 1

    for digit in num2_str:
        freq2[digit] = freq2.get(digit, 0) + 1

    # Check if the frequencies of digits are the same
    if freq1 == freq2:
        return True
    else:
        return False
