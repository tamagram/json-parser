from parser.constant import *


def parse_array(tokens):
    t = tokens[0]
    if t != LEFT_BRACKET:
        return None, tokens

    tokens = tokens[1:]
    arr = []
    while 0 < len(tokens):
        t = tokens[0]
        if t == RIGHT_BRACKET:
            return arr, tokens[1:]
        arr.append(t)
        tokens = tokens[1:]
    raise Exception("Excepted end-of-string RIGHT_BRACKET")
