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

    def test_object_in_array(self):
        arg = ["[", "a", "b", "c", "{", "user", ":", "hoge", "}", "]"]
        want = {"json_array": ["a", "b", "c", {"user": "hoge"}], "tokens": []}
        json_array, tokens = parse_array(arg)
        got = {"json_array": json_array, "tokens": tokens}
        self.assertEqual(want, got)

    def test_exception(self):
        arg = ["[", "a", "b"]
        with self.assertRaises(Exception):
            parse_array(arg)


class TestParseObject(unittest.TestCase):
    def test_object(self):
        arg = ["{", "user", ":", "hoge", "}"]
        want = {"json_object": {"user": "hoge"}, "tokens": []}
        json_object, tokens = parse_object(arg)
        got = {"json_object": json_object, "tokens": tokens}
        self.assertEqual(want, got)

    def test_array(self):
        arg = ["[", "a", "b", "c", "]"]
        want = {"json_object": None, "tokens": ["[", "a", "b", "c", "]"]}
        json_object, tokens = parse_object(arg)
        got = {"json_object": json_object, "tokens": tokens}
        self.assertEqual(want, got)

    def test_array_in_object(self):
        arg = [
            "{",
            "user",
            ":",
            "hoge",
            "posts",
            ":",
            "[",
            "a",
            "b",
            "c",
            "]",
            "}",
        ]
        want = {"json_object": {"user": "hoge", "posts": ["a", "b", "c"]}, "tokens": []}
        json_object, tokens = parse_object(arg)
        got = {"json_object": json_object, "tokens": tokens}
        self.assertEqual(want, got)

    def test_exception(self):
        arg = ["{", 3, ":", "hoge", "}"]
        with self.assertRaises(Exception):
            parse_object(arg)
        arg = ["{", "user", "hoge", "}"]
        with self.assertRaises(Exception):
            parse_object(arg)
        arg = ["{", "user", ":", "hoge"]
        with self.assertRaises(Exception):
            parse_object(arg)


# class TestParse(unittest.TestCase):
#     def test_json(self):
#         arg = [
#             "{",
#             "user",
#             ":",
#             "hoge",
#             "posts",
#             ":",
#             "[",
#             "a",
#             "b",
#             "c",
#             "]",
#             "}",
#         ]
#         want = {"user": "hoge", "posts": ["a", "b", "c"]}
#         got = parse(arg)
#         self.assertEqual(want, got)
