import unittest

from tokenType import TokenType, Token
from lexer import Lexer


class TestLexer(unittest.TestCase):

    def test_next_token(self):
        input = "=+(){},;"
        expected_tokens = [
            Token(TokenType.Assign, "="),
            Token(TokenType.Plus, "+"),
            Token(TokenType.LeftParen, "("),
            Token(TokenType.RightParen, ")"),
            Token(TokenType.LeftBrace, "{"),
            Token(TokenType.RightBrace, "}"),
            Token(TokenType.Comma, ","),
            Token(TokenType.Semicolon, ";"),
        ]

        lexer = Lexer(input)

        for expectedToken in expected_tokens:
            token = lexer.next_token()
            self.assertEqual(token.Type, expectedToken.Type)
            self.assertEqual(token.Literal, expectedToken.Literal)

