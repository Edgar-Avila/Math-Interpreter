from lexer import Lexer
from parser_ import Parser

def main():
    text = "-(1+2"
    # Lexical analysis
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()

    # Syntax analysis
    parser = Parser(tokens)
    tree = parser.parse()

    print(tree)

if __name__ == '__main__':
    main()
