from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    Illegal = 1,
    EOF = 2,

    Identifier = 3,
    Int = 4,

    Assign = 5,
    Plus = 6,

    Comma = 7,
    Semicolon = 8,

    LeftParen = 9,
    RightParen = 10,
    LeftBrace = 11,
    RightBrace = 12,

    Function = 13,
    Let = 14,


@dataclass
class Token:
    Type: TokenType
    Literal: str
