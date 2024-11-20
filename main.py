"""
Text to Morse Code Converter

Author: Alan
Date: November 20th 2024

Simple text to morse code converter, uses the text of the user and prints it.
"""

# Define the Morse code dictionary
morse_code = {
    # Letters
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    # Punctuation
    '.': '.-.-.-',  # Period
    ',': '--..--',  # Comma
    '?': '..--..',  # Question mark
    "'": '.----.',  # Apostrophe
    '!': '-.-.--',  # Exclamation mark
    '/': '-..-.',  # Slash
    '(': '-.--.',  # Open parenthesis
    ')': '-.--.-',  # Close parenthesis
    '&': '.-...',  # Ampersand
    ':': '---...',  # Colon
    ';': '-.-.-.',  # Semicolon
    '=': '-...-',  # Equals
    '+': '.-.-.',  # Plus
    '-': '-....-',  # Hyphen
    '_': '..--.-',  # Underscore
    '"': '.-..-.',  # Quotation marks
    '$': '...-..-',  # Dollar sign
    '@': '.--.-.'  # At sign
}

# Gets the text from the user
text = input("Please type your text: ")

# Initialize the morse_text variable
morse_text = ""

# For each character in the text:
for character in text:

    # Formats the character to upper (so it matches with the upper letters in the dictionary)
    formatted_character = character.upper()

    # If we find the character, we use the morse code by using the formatted_character as the key
    if formatted_character in morse_code:

        morse_text += morse_code[formatted_character] + " "

    # If we find a blank space, we replace it by three of them
    elif character == " ":

        morse_text += "   "

    # If we don't find anything, then we simply add it.
    else:

        morse_text += character

# Prints the text and removes any possible blank space at the end of our text
print(morse_text.strip())
