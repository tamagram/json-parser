import unittest
from lexer import *


class TestLexString(unittest.TestCase):
    def test_quote(self):
        arg = '{}'
        want = {
            "json_string": None,
            "string": '{}'
        }
        json_string, string = lex_string(arg)
        got = {
            "json_string": json_string,
            "string": string
        }
        self.assertEqual(want["json_string"], got["json_string"])
        self.assertEqual(want["string"], got["string"])

    def test_string(self):
        arg = '"hoge": 30'
        want = {
            "json_string": "hoge",
            "string": ": 30"
        }
        json_string, string = lex_string(arg)
        got = {
            "json_string": json_string,
            "string": string
        }
        self.assertEqual(want["json_string"], got["json_string"])
        self.assertEqual(want["string"], got["string"])

    def test_exception(self):
        arg = '"hoge'
        with self.assertRaises(Exception):
            lex_string(arg)


class TextLexer(unittest.TestCase):
    def test_lex(self):
        want = ['{', 'foo', ':', '[', 1, ',', 2,
                ',', '{', 'bar', ':', 2, '}', ']', '}']
        got = lex('{"foo": [1, 2, {"bar": 2}]}')
        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
