import unittest
from src.parser import LogParser
from src.models import LogEntry

class TestLogParser(unittest.TestCase):

    def setUp(self):
        self.parser = LogParser()

    def test_parse_valid_error_line(self):
        entry = self.parser.parse_line("2026-01-01 10:00:00 ERROR DB failed")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.status, "ERROR")
        self.assertEqual(entry.date, "2026-01-01")
        self.assertEqual(entry.time, "10:00:00")
        self.assertEqual(entry.message, "DB failed")

    def test_parse_valid_info_line(self):
        entry = self.parser.parse_line("2026-01-02 09:00:00 INFO Service started")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.status, "INFO")

    def test_parse_invalid_line_returns_none(self):
        entry = self.parser.parse_line("this is not a log line")
        self.assertIsNone(entry)

    def test_parse_empty_string_returns_none(self):
        entry = self.parser.parse_line("")
        self.assertIsNone(entry)

    def test_parse_all_skips_invalid(self):
        lines = [
            "2026-01-01 10:00:00 ERROR Valid line",
            "this is invalid",
            "2026-01-01 11:00:00 INFO Another valid line",
        ]
        entries = list(self.parser.parse_all(lines))
        self.assertEqual(len(entries), 2)

    def test_returns_log_entry_instance(self):
        entry = self.parser.parse_line("2026-01-01 10:00:00 WARNING Low memory")
        self.assertIsInstance(entry, LogEntry)


if __name__ == "__main__":
    unittest.main()