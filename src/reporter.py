class LogReporter:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def print_report(self):
        self._print_header()
        self._print_status_counts()
        self._print_top_messages()
        self._print_errors()
        self._print_summary()
        self._print_footer()

    def _print_header(self):
        print("=" * 45)
        print("         LOG ANALYSIS REPORT")
        print("=" * 45)

    def _print_status_counts(self):
        print("\n[1] Count by status:")
        counts = self.analyzer.count_by_status()
        for status, count in sorted(counts.items()):
            bar = "█" * count
            print(f"  {status:<10} : {count:>3}  {bar}")

    def _print_top_messages(self):
        print("\n[2] Top-5 most frequent messages:")
        top = self.analyzer.top_n_messages(5)
        for i, (msg, count) in enumerate(top, 1):
            print(f"  {i}. [{count}x] {msg}")

    def _print_errors(self):
        print("\n[3] ERROR entries:")
        errors = self.analyzer.filter_by_status("ERROR")
        if errors:
            for entry in errors:
                print(f"  {entry}")
        else:
            print("  No errors found.")

    def _print_summary(self):
        print("\n[4] Summary:")
        print(f"  Total entries  : {self.analyzer.total_count()}")
        print(f"  Valid entries  : {len(self.analyzer.get_valid_entries())}")

    def _print_footer(self):
        print("=" * 45)
