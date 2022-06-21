import unittest
from parser.parser import *


class TestParseArray(unittest.TestCase):
    def test_array(self):
        arg = ["[", "a", "b", "c", "]"]
        want = {"json_array": ["a", "b", "c"], "tokens": []}
        json_array, tokens = parse_array(arg)
        got = {"json_array": json_array, "tokens": tokens}
        self.assertEqual(want, got)

    def test_object(self):
        arg = ["{", "user", ":", "hoge", "}"]
        want = {"json_array": None, "tokens": ["{", "user", ":", "hoge", "}"]}
        json_array, tokens = parse_array(arg)
        got = {"json_array": json_array, "tokens": tokens}
        self.assertEqual(want, got)

    def test_exception(self):
        arg = ["[", "a", "b"]
        with self.assertRaises(Exception):
            parse_array(arg)
