import sys
import string

def text_analyzer(text):
    """
    Analyzes a given text and provides counts of different types of characters.

    This function takes a string as input and counts the following:
    - Printable characters
    - Uppercase letters
    - Lowercase letters
    - Spaces
    - Punctuation characters

    Parameters:
    text (str): The input string to be analyzed.

    Returns:
    None: The function prints the results directly.

    Example:
    >>> text_analyzer("Hello, Oussama 1880")
    Printable characters: 19
    Uppercase letters: 2
    Lowercase letters: 10
    Spaces: 2
    Punctuation characters: 1
    """
    if not isinstance(text, str):
        print("Invalid input")
        return

    printable = 0
    upper = 0
    lower = 0
    space = 0
    punc = 0

    for char in text:
        printable += char.isprintable()
        upper += char.isupper()
        lower += char.islower()
        space += char.isspace()
        punc += char in string.punctuation

    print("Printable characters: " + str(printable)) #concatenation
    print(f"Uppercase letters: {upper}") #f-string
    print("Lowercase letters: {}".format(lower)) #.format()
    print(f"Spaces: {space}")
    print(f"Punctuation characters: {punc}")

