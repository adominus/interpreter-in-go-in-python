from tokenType import TokenType, Token


class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.readPosition = 0
        self.ch = ""
        self._read_char()

    def next_token(self):
        token = None

        if self.ch == '=':
            token = Token(TokenType.Assign, self.ch)
        elif self.ch == ';':
            token = Token(TokenType.Semicolon, self.ch)
        elif self.ch == '(':
            token = Token(TokenType.LeftParen, self.ch)
        elif self.ch == ')':
            token = Token(TokenType.RightParen, self.ch)
        elif self.ch == ',':
            token = Token(TokenType.Comma, self.ch)
        elif self.ch == '+':
            token = Token(TokenType.Plus, self.ch)
        elif self.ch == '{':
            token = Token(TokenType.LeftBrace, self.ch)
        elif self.ch == '}':
            token = Token(TokenType.RightBrace, self.ch)
        elif self.ch == '\0':
            token = Token(TokenType.EOF, "")

        self._read_char()
        return token

    def _read_char(self):
        if self.readPosition >= len(self.input):
            self.ch = "\0"
        else:
            self.ch = self.input[self.readPosition]

        self.position = self.readPosition
        self.readPosition += 1
