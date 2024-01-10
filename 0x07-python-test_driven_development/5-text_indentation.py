#!/usr/bin/python3
"""
Module to print a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function to print a text with 2 new lines after each of ., ? and :

    Args:
        text (str): Input text

    Raises:
        TypeError: If text is not a string
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the text
    for char in text:
        # Append the character to the result string
        result += char

        # If the character is ., ?, or :, add 2 new lines to the result string
        if char in '.?:':
            result += '\n\n'

    # Print the formatted text
    print(result, end="")


if __name__ == "__main__":
    # Example usage
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

