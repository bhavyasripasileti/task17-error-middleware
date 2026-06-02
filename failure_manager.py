from datetime import datetime

class FailureManager:
    def __init__(self):
        self.failures = []

    def log_failure(self, error):
        self.failures.append({
            "error": str(error),
            "timestamp": datetime.now().isoformat()
        })

    def get_failures(self):
        return self.failures


failure_manager = FailureManager()