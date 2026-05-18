class LogEntry:

    VALID_STATUSES = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}

    def __init__(self, date, time, status, message):
        self.date = date
        self.time = time
        self.status = status
        self.message = message

    def is_valid(self):
        return self.status in self.VALID_STATUSES

    def __repr__(self):
        return f"[{self.date} {self.time}] {self.status}: {self.message}"

    def __eq__(self, other):
        if not isinstance(other, LogEntry):
            return False
        return (self.date == other.date and self.time == other.time and
                self.status == other.status and self.message == other.message)

