import re
from src.models import LogEntry


class LogParser:


    PATTERN = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"

    def parse_line(self, line):

        match = re.match(self.PATTERN, line)
        if match:
            date, time, status, message = match.groups()
            return LogEntry(date, time, status, message)
        return None

    def parse_all(self, lines):

        for line in lines:
            entry = self.parse_line(line)
            if entry is not None:
                yield entry