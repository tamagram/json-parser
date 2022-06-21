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


class TestLexNumber(unittest.TestCase):
    def test_number(self):
        arg = "3"
        want = {
            "json_number": 3,
            "string": ""
        }
        json_number, string = lex_number(arg)
        got = {
            "json_number": json_number,
            "string": string
        }
        self.assertEqual(want["json_number"], got["json_number"])
        self.assertEqual(want["string"], got["string"])

    def test_string(self):
        arg = "a"
        want = {
            "json_number": None,
            "string": "a"
        }
        json_number, string = lex_number(arg)
        got = {
            "json_number": json_number,
            "string": string
        }
        self.assertEqual(want["json_number"], got["json_number"])
        self.assertEqual(want["string"], got["string"])


class TestLexSyntax(unittest.TestCase):
    def test_syntax(self):
        arg = "{}"
        want = {
            "json_syntax": "{",
            "string": "}"
        }
        json_syntax, string = lex_syntax(arg)
        got = {
            "json_syntax": json_syntax,
            "string": string
        }
        self.assertEqual(want["json_syntax"], got["json_syntax"])
        self.assertEqual(want["string"], got["string"])

    def test_string(self):
        arg = "a"
        want = {
            "json_syntax": None,
            "string": "a"
        }
        json_syntax, string = lex_syntax(arg)
        got = {
            "json_syntax": json_syntax,
            "string": string
        }
        self.assertEqual(want["json_syntax"], got["json_syntax"])
        self.assertEqual(want["string"], got["string"])


class TextLexer(unittest.TestCase):
    def test_lex(self):
        arg = '{"foo": [1, 2, {"bar": 2}]}'
        want = ['{', 'foo', ':', '[', 1, ',', 2,
                ',', '{', 'bar', ':', 2, '}', ']', '}']
        got = lex(arg)
        self.assertEqual(want, got)

    def test_exception(self):
        arg = '{"foo": [1, 2~, {"bar": 2}]}'
        with self.assertRaises(Exception):
            lex(arg)


if __name__ == '__main__':
    unittest.main()
