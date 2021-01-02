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
            self.assertEqual(expectedToken, token)

    def test_next_token(self):
        input = "let five = 5;" \
                "let ten = 10;" \
                "" \
                "let add = fn(x, y) {" \
                "x + y;" \
                "};" \
                "" \
                "let result = add(five, ten);" \
                "";

        expected_tokens = [
            Token(TokenType.Let, "let"),
            Token(TokenType.Identifier, "five"),
            Token(TokenType.Assign, "="),
            Token(TokenType.Int, "5"),
            Token(TokenType.Semicolon, ";"),
            Token(TokenType.Let, "let"),
            Token(TokenType.Identifier, "ten"),
            Token(TokenType.Assign, "="),
            Token(TokenType.Int, "10"),
            Token(TokenType.Semicolon, ";"),
            Token(TokenType.Let, "let"),
            Token(TokenType.Identifier, "add"),
            Token(TokenType.Assign, "="),
            Token(TokenType.Function, "fn"),
            Token(TokenType.LeftParen, "("),
            Token(TokenType.Identifier, "x"),
            Token(TokenType.Comma, ","),
            Token(TokenType.Identifier, "y"),
            Token(TokenType.RightParen, ")"),
            Token(TokenType.LeftBrace, "{"),
            Token(TokenType.Identifier, "x"),
            Token(TokenType.Plus, "+"),
            Token(TokenType.Identifier, "y"),
            Token(TokenType.Semicolon, ";"),
            Token(TokenType.RightBrace, "}"),
            Token(TokenType.Semicolon, ";"),
            Token(TokenType.Let, "let"),
            Token(TokenType.Identifier, "result"),
            Token(TokenType.Assign, "="),
            Token(TokenType.Identifier, "add"),
            Token(TokenType.LeftParen, "("),
            Token(TokenType.Identifier, "five"),
            Token(TokenType.Comma, ","),
            Token(TokenType.Identifier, "ten"),
            Token(TokenType.RightParen, ")"),
            Token(TokenType.Semicolon, ";"),
        ]

        lexer = Lexer(input)

        for expectedToken in expected_tokens:
            token = lexer.next_token()
            self.assertEqual(expectedToken, token)

