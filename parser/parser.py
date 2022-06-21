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


def parse_object(tokens):
    t = tokens[0]
    if t != LEFT_BRACE:
        return None, tokens

    tokens = tokens[1:]
    obj = {}
    while 0 < len(tokens):
        t = tokens[0]
        if t == RIGHT_BRACE:
            return obj, tokens[1:]

        key = tokens.pop(0)
        if type(key) is not str:
            raise Exception("Expected string key, got: {}".format(key))

        colon = tokens.pop(0)
        if colon != COLON:
            raise Exception('Expected colon after key in object, got: {}'.format(colon))
        
        value = tokens.pop(0)
        obj[key] = value
    raise Exception('Expected end-of-object bracket')