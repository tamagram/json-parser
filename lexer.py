import json


COMMA = ','
COLON = ':'
LEFT_BRACKET = '['
RIGHT_BRACKET = ']'
LEFT_BRACE = '{'
RIGHT_BRACE = '}'
QUOTE = '"'
SYNTAX = [COMMA, COLON, LEFT_BRACKET, RIGHT_BRACKET, LEFT_BRACE, RIGHT_BRACE]

WHITESPACE = [' ', '\t', '\b', '\n', '\r']


def lex_string(text):
    if text[0] != QUOTE:
        return None, text

    json_string = ""
    text = text[1:]
    for c in text:
        if c == QUOTE:
            next_text = text[len(json_string)+1:]
            return json_string, next_text
        else:
            json_string += c

    raise Exception("Excepted end-of-string quote")


def lex(text):
    tokens = []
    while 0 < len(text):
        print(text)
        
        json_string, next_text = lex_string(text)
        if json_string is not None:
          tokens.append(json_string)
          text = next_text
          continue
        
        c = text[0]
        if c in WHITESPACE:
            next_text = text[1:]
        elif c in SYNTAX:
            tokens.append(c)
            next_text = text[1:]
        else:
            pass

        text = next_text
    return tokens
