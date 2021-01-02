from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    Illegal = 1,
    EOF = 2,

    Identifier = 3,
    Int = 4,

    Assign = 5,
    Plus = 6,
    Minus = 7,
    Bang = 8,
    Asterisk = 9,
    Slash = 10,

    LT = 11,
    GT = 12,

    Comma = 13,
    Semicolon = 14,

    LeftParen = 15,
    RightParen = 16,
    LeftBrace = 17,
    RightBrace = 18,

    Function = 19,
    Let = 20,
    TrueKeyword = 21,
    FalseKeyword = 22,
    If = 23,
    Else = 24,
    Return = 25,


@dataclass
class Token:
    Type: TokenType
    Literal: str


def lookup_identifier_token_type(identifier):
    if identifier == "fn":
        return TokenType.Function
    elif identifier == "let":
        return TokenType.Let
    elif identifier == "true":
        return TokenType.TrueKeyword
    elif identifier == "false":
        return TokenType.FalseKeyword
    elif identifier == "if":
        return TokenType.If
    elif identifier == "else":
        return TokenType.Else
    elif identifier == "return":
        return TokenType.Return

    return TokenType.Identifier
