"""Made to test my memory on the parts of a compiler"""


PLUS,MINUS = 'PLUS','MINUS'
INTEGER    = 'INTEGER'
EOF        = 'EOF'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = repr(value)
    
    def __str__(self):
        return "Token({},{})".format(
            self.type,
            self.value
        )
    
    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, stream):
        self.stream = stream
        self.pos   = 0
        self.current_character = self.stream[0]
        self.current_token     = None
    
    def error(self):
        raise Exception("Syntax Error")

    def skip_whitespace(self):
        while self.current_character is not None and self.current_character.isspace():
            self.advance()

    def get_next_token(self):
        while self.current_character is not None:
            if self.current_character.isdigit():v 
                return Token(INTEGER, self.integer())
            
            if self.current_character.isspace():
                self.skip_whitespace()
                continue

            if self.current_token in (PLUS, MINUS):
                if self.current_token == PLUS:
                    self.advance()
                    return Token(PLUS, '+')
                if self.current_token == MINUS:
                    self.advance()
                    return Token(MINUS, '-')
            
            self.error()
        return Token(EOF, None)

    def advance(self):
        self.pos += 1
        if self.pos > len(self.stream) - 1:
            self.current_token = None
        else:
            self.current_character = self.stream[self.pos]

    def integer(self):
        result = ''
        while self.current_character.isdigit():
            result += self.current_character
            self.advance
        return int(result)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()
    
