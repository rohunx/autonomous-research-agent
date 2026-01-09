class Memory:
    def __init__(self):
        self.history = []

    def add(self, entry):
        self.history.append(entry)

    def get(self):
        return "\n".join(self.history)
