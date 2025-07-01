class LoggerObj:
    def __init__(self, log_file: str):
        self.log_file = log_file

    def __str__(self):
        return f'{self.log_file}'