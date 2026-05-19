from src.loader import LogLoader
from src.parser import LogParser
from src.analyzer import LogAnalyzer
from src.reporter import LogReporter
from src.cli import timer, get_user_filter, get_date_range

DATA_FILE = "data/sample.log"


@timer
def run_analysis(status_filter=None, start_date=None, end_date=None):

    loader = LogLoader(DATA_FILE)
    parser = LogParser()

    raw_lines = loader.load()
    entries = list(parser.parse_all(raw_lines))

    analyzer = LogAnalyzer(entries)

    if status_filter:
        entries = analyzer.filter_by_status(status_filter)
        analyzer = LogAnalyzer(entries)

    if start_date and end_date:
        entries = analyzer.filter_by_date_range(start_date, end_date)
        analyzer = LogAnalyzer(entries)

    reporter = LogReporter(analyzer)
    reporter.print_report()


def main():
    print("=== Log Analyzer ===")
    print(f"Analyzing: {DATA_FILE}")

    status = get_user_filter()
    start, end = get_date_range()

    run_analysis(status_filter=status, start_date=start, end_date=end)


if __name__ == "__main__":
    main()