import unittest
from src.models import LogEntry
from src.parser import LogParser
from src.analyzer import LogAnalyzer

class TestLogParser(unittest.TestCase):

    def setUp(self):
        self.parser = LogParser()

    def test_parse_valid_line(self):
        entry = self.parser.parse_line("2026-01-01 10:00:00 ERROR DB failed")

        self.assertIsNotNone(entry)
        self.assertEqual(entry.status, "ERROR")
        self.assertEqual(entry.date, "2026-01-01")
        self.assertEqual(entry.message, "DB failed")

    def test_parse_invalid_line(self):
        entry = self.parser.parse_line("this is not a log line")
        self.assertIsNone(entry)

    def test_parse_empty_line(self):
        entry = self.parser.parse_line("")
        self.assertIsNone(entry)


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.entries = [
            LogEntry("2026-01-01", "10:00:00", "ERROR", "DB error"),
            LogEntry("2026-01-01", "10:01:00", "INFO", "Started"),
            LogEntry("2026-01-02", "10:02:00", "ERROR", "DB error"),
            LogEntry("2026-01-02", "10:03:00", "WARNING", "Low memory"),
            LogEntry("2026-01-03", "10:04:00", "INFO", "Started"),
        ]

        self.analyzer = LogAnalyzer(self.entries)

    def test_count_by_status(self):
        counts = self.analyzer.count_by_status()

        self.assertEqual(counts["ERROR"], 2)
        self.assertEqual(counts["INFO"], 2)
        self.assertEqual(counts["WARNING"], 1)

    def test_top_messages(self):
        top = self.analyzer.top_n_messages(1)

        self.assertEqual(top[0][0], "DB error")
        self.assertEqual(top[0][1], 2)

    def test_filter_by_status(self):
        errors = self.analyzer.filter_by_status("ERROR")

        self.assertEqual(len(errors), 2)

        for e in errors:
            self.assertEqual(e.status, "ERROR")

    def test_filter_by_date_range(self):
        result = self.analyzer.filter_by_date_range("2026-01-01", "2026-01-02")
        self.assertEqual(len(result), 4)

    def test_total_count(self):
        self.assertEqual(self.analyzer.total_count(), 5)



if __name__ == "__main__":
    unittest.main()