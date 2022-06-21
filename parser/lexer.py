from parser.constant import *

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


def lex_number(text):
    number_character = [str(d) for d in range(10)] + ["-", ".", "e"]

    json_number = ""
    for c in text:
        if c in number_character:
            json_number += c
        else:
            break

    next_text = text[len(json_number):]
    if json_number == "":
        return None, text
    else:
        return int(json_number), next_text


def lex_syntax(text):
    if text[0] in SYNTAX:
        return text[0], text[1:]
    else:
        return None, text


def lex(text):
    tokens = []
    while 0 < len(text):
        json_string, text = lex_string(text)
        if json_string is not None:
            tokens.append(json_string)
            continue

        json_number, text = lex_number(text)
        if json_number is not None:
            tokens.append(json_number)
            continue

        json_syntax, text = lex_syntax(text)
        if json_syntax is not None:
            tokens.append(json_syntax)
            continue

        c = text[0]
        if c in WHITESPACE:
            text = text[1:]
            continue
        raise SyntaxError("Unexpected character {}".format(c))

    return tokens
