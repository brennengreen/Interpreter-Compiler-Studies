# Grammar to convert:
#       expr : factor((MUL | DIV)factor)*
#       factor : INTEGER

# Rules becomes a method
def factor(self):
    # Tokens become a call to eat
    self.eat(INTEGER)

def expr():
    self.factor()

    # Option Groupings become while loops
    while self.current_token.type in (MUL, DIV):
        token = self.current_token
        # Alternatives become if else structures
        if token.type == MUL:
            self.eat(MUL)
            self.factor()
        if token.type == DIV:
            self.eat(DIV)
            self.factor()


