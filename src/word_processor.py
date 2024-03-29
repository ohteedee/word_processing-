"""
Create a function that counts the number
of words in a string
Make sure to run all tests and run the commands:
 coverage run -m pytest
 and
coverage html
to get the coverage of tests.
Open the index.html in the browser.
"""

# hello there

def count_words(text):
    """
    This function counts some words and return integer which is the length of wordsg
    """
    if not isinstance(text, str):
        raise TypeError("only accepts strings")

    special_characters = ['-', '+', '\n']

    for character in special_characters:
        text = text.replace(character, " ")

    words = text.split()
    return len(words)


if __name__ == "__main__":
    SOME_WORDS= "everlyn\nTosin"
    print(count_words(SOME_WORDS))
