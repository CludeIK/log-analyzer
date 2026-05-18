# Log Analyzer

A Python application for analyzing system log files.

## Team Members
- Imangali Kabiyev — Project setup, LogEntry model, main runner
- Arnur Kudaibergen — Log file loader and parser (regex)
- Bazarkul Balnur — Log analyzer (statistics, top-N)
- Ayazhan Rakhymbay — Log filter (by status, by date)
- Nurlybek Sultan — Decorators, CLI, tests

## How to Run

```bash
python main.py
```

## Project Structure
```
glog-analyzer/
├── src/
│   ├── models.py       # LogEntry data model
│   ├── loader.py       # File reading with generator
│   ├── parser.py       # Regex line parsing
│   ├── analyzer.py     # Statistics and aggregation
│   ├── reporter.py     # Output formatting
│   └── cli.py          # Command-line interface
├── tests/              # Unit tests
├── data/
│   └── sample.log      # Sample log file
└── main.py             # Entry point
```
## Input Format
```
YYYY-MM-DD HH:MM:SS STATUS message
```
## Supported Status Levels
- DEBUG, INFO, WARNING, ERROR, CRITICAL