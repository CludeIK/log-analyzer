import unittest
from src.loader import LogLoader

class TestLogLoader(unittest.TestCase):

    def test_load_returns_lines(self):
        loader = LogLoader("data/sample.log")
        lines = list(loader.load())
        self.assertGreater(len(lines), 0)

    def test_all_lines_are_strings(self):
        loader = LogLoader("data/sample.log")
        for line in loader.load():
            self.assertIsInstance(line, str)

    def test_no_empty_lines(self):
        loader = LogLoader("data/sample.log")
        lines = list(loader.load())
        for line in lines:
            self.assertNotEqual(line.strip(), "")

    def test_file_not_found(self):
        loader = LogLoader("data/nonexistent.log")
        with self.assertRaises(FileNotFoundError):
            list(loader.load())


if __name__ == "__main__":
    unittest.main()