# Define the Morse code dictionary
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Function to convert a string to Morse code
def to_morse_code(string):
    morse_code = ""
    for char in string:
        # Check if the character is in the Morse code dictionary
        if char.upper() in morse_dict:
            morse_code += morse_dict[char.upper()] + " "
        else:
            morse_code += " "
    return morse_code

# Prompt the user for input
string = input("Enter a string to convert to Morse code: ")

# Convert the string to Morse code
morse_code = to_morse_code(string)

# Print the Morse code
print("Morse code: " + morse_code)
