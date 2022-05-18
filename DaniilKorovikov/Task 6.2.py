class HistoryDict():
    def __init__(self, d: dict):
        self.d = d
        self.history = []

    def set_value(self, key, value):
        self.d[key] = value
        if len(self.history) < 10:
            self.history.append(key)
        else:
            self.history.pop(0)
            self.history.append(key)

    def get_history(self):
        print(self.history)


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()
