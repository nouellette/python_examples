class MovingAverages:
    def __init__(self, window_size):
        self.window_size = window_size
        self.values = []
        self.sum = 0

    def add_values(self, value):
        self.values.append(value)
        self.sum += value
        if (len(self.values) > self.window_size):
            self.sum -= self.values.pop(0)

    def get_average(self):
        return self.sum / min(len(self.values), self.window_size)


ma = MovingAverages(1)
ma.add_values(1)
ma.add_values(3)
print(ma.get_average())