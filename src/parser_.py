from tokens import TokenType, Token
from nodes import *

PLUS_MINUS = (TokenType.PLUS, TokenType.MINUS)
MULT_DIV = (TokenType.MULTIPLY, TokenType.DIVIDE)

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = iter(tokens)
        self.current_token: Token | None = None
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None
        result = self.expr()

        if self.current_token != None:
            self.raise_error()

        return result

    def expr(self):
        result = self.term()

        while self.current_token != None and self.current_token.type in PLUS_MINUS:
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubNode(result, self.term())
        return result

    def term(self):
        result = self.factor()

        while self.current_token != None and self.current_token.type in MULT_DIV:
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivNode(result, self.factor())
        return result

    def factor(self):
        token = self.current_token
        if token == None:
            self.raise_error()

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()
            if self.current_token == None:
                self.raise_error()
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            self.advance()
            return result
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())
        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())
        
        self.raise_error()
