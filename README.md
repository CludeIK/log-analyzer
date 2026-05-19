# Log Analyzer

A Python application for analyzing and filtering system log files.

## Team Members
- Imangali Kabiyev — Project setup, LogEntry model, main runner
- Arnur Kudaibergen — Log file loader (generator) and parser (regex)
- Bazarkul Balnur — Log analyzer (statistics, top-N, filtering)
- Ayazhan Rakhymbay — Log reporter (formatted output)
- Nurlybek Sultan — Decorators, CLI interface, unit tests

## How to Run

```bash
python main.py
```

Then follow the prompts:
- Enter a status to filter by (DEBUG / INFO / WARNING / ERROR / CRITICAL) or press Enter to skip
- Enter a date range (YYYY-MM-DD) or press Enter to skip

## Example Output

```
=== Log Analyzer ===
Analyzing: data/sample.log

Filter by status (or press Enter to skip):
  Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
  Enter status: ERROR

=============================================
         LOG ANALYSIS REPORT
=============================================
[1] Count by status:
  ERROR      :   3  ███

[2] Top-5 most frequent messages:
  1. [2x] Failed to connect to database
  2. [1x] Timeout exceeded

[3] ERROR entries:
  [2026-01-01 10:15:32] ERROR: Failed to connect to database
  [2026-01-02 09:05:11] ERROR: Failed to connect to database
  [2026-01-03 08:31:00] ERROR: Timeout exceeded

[4] Summary:
  Total entries  : 3
  Valid entries  : 3
=============================================
[Timer] run_analysis executed in 0.0012 sec
```

## How to Run Tests

```bash
python -m unittest discover tests/
```

Expected output: 18 tests, all passing.

## Project Structure

```
log-analyzer/
├── src/
│   ├── models.py       # LogEntry data model
│   ├── loader.py       # File reading with generator
│   ├── parser.py       # Regex line parsing
│   ├── analyzer.py     # Statistics and aggregation
│   ├── reporter.py     # Formatted console output
│   └── cli.py          # Timer decorator and CLI input
├── tests/
│   ├── test_analyzer.py
│   ├── test_loader.py
│   └── test_parser.py
├── data/
│   └── sample.log      # Sample log file
├── main.py             # Entry point
└── README.md
```

## Input Format

```
YYYY-MM-DD HH:MM:SS STATUS message
```

## Supported Status Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

## Key Technical Decisions

- **Generator** in `LogLoader` and `LogParser` — reads file line by line without loading everything into memory
- **Regex** in `LogParser` — reliable pattern matching for structured log lines
- **Set** for `VALID_STATUSES` in `LogEntry` — O(1) lookup instead of O(n) list scan
- **lambda + map/filter** in `LogAnalyzer` — concise functional-style data processing
- **@timer decorator** in `cli.py` — measures execution time without modifying core logic