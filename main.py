
# the morse code dictionary was generated using claude.ai
morse_dict = {
    # Letters
    'A': '%-',    'B': '%_..',  'C': '%_._',  'D': '%..',   'E': '.',
    'F': '.._.',  'G': '__.',   'H': '....',  'I': '..',    'J': '.___',
    'K': '_.-',   'L': '._..',  'M': '__',    'N': '_.',    'O': '___',
    'P': '.__.',  'Q': '__._',  'R': '._.',   'S': '...',   'T': '_',
    'U': '.._',   'V': '..._',  'W': '.__',   'X': '_.._',  'Y': '_.__',
    'Z': '__..',
    
    # Numbers
    '0': '^____', '1': '^.___', '2': '^..___', '3': '^...__', '4': '^...._',
    '5': '^.....', '6': '^_....', '7': '^__...', '8': '^___..', '9': '^____.',
    
    # Special Characters
    ' ': '%%',      # Space
    '.': '._._._',  # Period
    ',': '__..__',  # Comma
    '?': '..__.',   # Question mark
    '!': '_._.__',  # Exclamation mark
    '-': '_...._',  # Hyphen/dash
    '/': '_.._.',   # Forward slash
    '@': '.__._.',  # At symbol
    '(': '_.__.',   # Opening parenthesis
    ')': '_.__._',  # Closing parenthesis
    '&': '.-...',   # Ampersand
    ':': '___...',  # Colon
    ';': '_._._.',  # Semicolon
    '=': '_..._',   # Equals
    '+': '._._.',   # Plus
    '"': '._.._.',  # Quotation mark
    "'": '.____.',  # Apostrophe
    '$': '..._.._', # Dollar sign
}


keep_translating = True
while keep_translating:
    todo = input("\nType 'g' to generate morse code or 't' to translate morse code or 'end' to end program: ").lower()

    if todo == 'g':
        message = input("What is your message?\n    ")
        morse_code = ""
        for char in message.upper():
            morse_code += morse_dict[char] + '¬' # '¬' is the delimiter
        print("\n\n", morse_code)

    elif todo == 't':
        morse_code = input("What is your morse code?\n    ")
        morse_code = morse_code.split("¬")
        translation = ""
        for char in morse_code:
            try:
                translation += list(morse_dict.keys())[list(morse_dict.values()).index(char)]
            except ValueError:
                translation += char                      
        print("\n\n", translation.lower())

    elif todo == 'end':
        keep_translating = False
            
    else:
        print("Invalid option. Please try again.")