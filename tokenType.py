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

    EQ = 11,
    NOT_EQ = 12,
    LT = 13,
    GT = 14,

    Comma = 15,
    Semicolon = 16,

    LeftParen = 17,
    RightParen = 18,
    LeftBrace = 19,
    RightBrace = 20,

    Function = 21,
    Let = 22,
    TrueKeyword = 23,
    FalseKeyword = 24,
    If = 25,
    Else = 26,
    Return = 27,


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
