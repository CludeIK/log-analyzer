from src.models import LogEntry

DATA_FILE = "data/sample.log"

def main():
    print("=== Log Analyzer ===")
    print(f"Analyzing {DATA_FILE}")
    print()

    test_entry = LogEntry("2026-01-01", "10:00:00", "ERROR", "Test message")
    print(f"Test LogEntry: {test_entry}")
    print(f"Is valid: {test_entry.is_valid()}")
    print()

    # loader = LogLoader(DATA_FILE)
    # entries = list(loader.load())
    # analyzer = LogAnalyzer(entries)
    # reporter = LogReporter(analyzer)
    # reporter.print_report()

if __name__ == "__main__":
    main()