from tokens import TokenType, Token

WHITESPACE = ' \n\t'
DIGITS = '1234567890'
NUMBER_CHARS = DIGITS + '.'

class Lexer:
    def __init__(self, text) -> None:
        self.text = iter(text)
        self.current_char: str | None = ''
        self.advance()
    
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in NUMBER_CHARS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f'Illegal character {self.current_char}')


    def generate_number(self):
        decimal_point_count = 0
        number_str: str = self.current_char if self.current_char else ''
        self.advance()

        # Build the number into the number_str variable
        while self.current_char != None and self.current_char in NUMBER_CHARS:
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break
            number_str += self.current_char
            self.advance()

        # Complete numbers that start or end with a decimal point
        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str = number_str + '0'

        return Token(TokenType.NUMBER, float(number_str))
