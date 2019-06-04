# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis

INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
	def __init__(self, type, value):
		# token type: INTEGER, PLUS, EOF
		self.type = type
		self.value = value

	def __str__(self):
		# String represenation of token		#
		# Example: Token(INTEGER, 3)		#
		#		   Token(PLUS, '+')			#
		return "Token({type}, {value})".format(
			type=self.type,
			value=self.value
		)
	
	def __repr__(self):
		return self.__str__()

class Interpreter(object):
	def __init__(self, text):
		# client string input, e.g. "3+5"
		self.text = text
		# self.pos is an index ingto self.text
		self.pos = 0
		# current token instance
		self.current_token = None
	
	def error(self):
		raise Exception("Error Parsing Input")
	
	def get_next_token(self):
		# Lexical Analyzer (aka Scanner/Tokenizer) #
		#                                          #
		# This method is responsible for breaking  #
		# breaking a sentence apart into token.    #
		text = self.text

		# Check if Interpreter is at end of input
		if self.pos > len(text) - 1:
			return Token(EOF, None)
		
		current_char = text[self.pos]

		if current_char.isdigit():
			token = Token(INTEGER, int(current_char))
			self.pos += 1
			return token
		
		if current_char == '+':
			token = Token(PLUS, current_char)
			self.pos += 1
			return token
		
		self.error()
	
	def eat(self, token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()

	def expr(self):
		"""expr -> INTEGER PLUS INTEGER"""
		self.current_token = self.get_next_token()

		left = self.current_token
		self.eat(INTEGER)

		operation = self.current_token
		self.eat(PLUS)

		right = self.current_token
		self.eat(INTEGER)

		if operation.type == PLUS:
			return left.value + right.value

def main():
	while True:
		try:
			text = input("calc> ")
		except EOFError:
			break
		if not text:
			continue
		
		print(Interpreter(text).expr())

if __name__ == "__main__":
	main()