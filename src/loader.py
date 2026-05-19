class LogLoader:

    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield line