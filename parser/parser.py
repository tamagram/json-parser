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
        elif t == LEFT_BRACKET:
            t, tokens = parse_array(tokens)
        elif t == LEFT_BRACE:
            t, tokens = parse_object(tokens)
        else:
            tokens = tokens[1:]
        arr.append(t)
    raise Exception("Excepted end-of-string RIGHT_BRACKET")
    # return ["a", "b", "c", {"user": "hoge"}], []


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
        
        value = tokens[0]
        if value == LEFT_BRACKET:
            value, tokens = parse_array(tokens)
        elif value == LEFT_BRACE:
            value, tokens = parse_object(tokens)
        else:
            tokens = tokens[1:]
        obj[key] = value
        
        
    raise Exception('Expected end-of-object bracket')

# def parse(tokens):
#     json = []
#     while 0 < len(tokens):
#         json_array, tokens = parse_array(tokens)
#         if json_array is not None:
#             json.append(json_array)
#             continue

#         json_object, tokens = parse_object(tokens)
#         if json_object is not None:
#             json.append(json_object)
#             continue
        
#         return json, tokens