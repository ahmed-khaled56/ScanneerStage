import re
from enum import Enum, auto

# Define TokenType enum for different token types
class TokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    NUMBER = auto()
    STRING = auto()
    COMMENT = auto()
    OPERATOR = auto()
    SPECIAL_CHAR = auto()
    UNKNOWN = auto()

# Define Token class to store each token's type and lexeme
class Token:
    def __init__(self, type, lexeme):
        self.type = type
        self.lexeme = lexeme

    def __str__(self):
        return f"Token: {self.lexeme:<15} Type: {self.type.name}"

# List of keywords in C language
KEYWORDS = {"int", "float", "return", "if", "else", "while", "for", "char"}

# Regular expression patterns for each token type
PATTERNS = {
    TokenType.IDENTIFIER: r'^[a-zA-Z_][a-zA-Z0-9_]*',
    TokenType.NUMBER: r'^\d+',
    TokenType.STRING: r'^"(.*?)"',
    TokenType.COMMENT: r'^//.*',
    TokenType.OPERATOR: r'^[+\-*/=<>!&|]+',
    TokenType.SPECIAL_CHAR: r'^[;,(){}]',
}

# Function to get the next token from the input text
def get_next_token(text):
    # Skip leading whitespace
    text = text.lstrip()

    # Check each pattern
    for token_type, pattern in PATTERNS.items():
        match = re.match(pattern, text)
        if match:
            lexeme = match.group(0)
            if token_type == TokenType.IDENTIFIER and lexeme in KEYWORDS:
                return Token(TokenType.KEYWORD, lexeme), text[len(lexeme):]
            return Token(token_type, lexeme), text[len(lexeme):]

    # If no pattern matches, return the first character as UNKNOWN
    if text:
        return Token(TokenType.UNKNOWN, text[0]), text[1:]
    return None, ''  # End of input

# Function to tokenize the entire input text
def tokenize(input_text):
    tokens = []
    text = input_text
    while text:
        token, text = get_next_token(text)
        if token:
            tokens.append(token)
    return tokens

# Main function to run the scanner
def main():
    print("Enter expressions to scan. Type 'done' to finish.")
    while True:
        input_text = input("Enter an expression: ")
        if input_text.strip().lower() == "done":
            print("Finished testing.")
            break
        tokens = tokenize(input_text)
        for token in tokens:
            print(token)
        print()  # Blank line for readability between inputs

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
