from collections import Counter


class LogAnalyzer:
    """Анализирует список LogEntry — считает статистику."""

    def __init__(self, entries):
        self.entries = list(entries)

    def count_by_status(self):
        """Считает количество записей по каждому статусу."""
        statuses = list(map(lambda e: e.status, self.entries))
        return dict(Counter(statuses))

    def top_n_messages(self, n=5):
        """Возвращает топ-N самых частых сообщений."""
        messages = list(map(lambda e: e.message, self.entries))
        return Counter(messages).most_common(n)

    def filter_by_status(self, status):
        """Фильтрует записи по статусу (например ERROR)."""
        return list(filter(lambda e: e.status == status, self.entries))

    def filter_by_date_range(self, start_date, end_date):
        """Фильтрует записи по диапазону дат. Формат: YYYY-MM-DD"""
        return list(filter(lambda e: start_date <= e.date <= end_date, self.entries))

    def get_valid_entries(self):
        """Возвращает только валидные записи."""
        return list(filter(lambda e: e.is_valid(), self.entries))

    def total_count(self):
        """Общее количество записей."""
        return len(self.entries)
