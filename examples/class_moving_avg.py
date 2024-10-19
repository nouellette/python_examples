class MovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
        self.values = []
        self.sum = 0

    def add_value(self, value):
        self.values.append(value)
        self.sum += value
        if len(self.values) > self.window_size:
            self.sum -= self.values.pop(0)

    def get_average(self):
        if not self.values:
            return 0
        return self.sum / min(len(self.values), self.window_size)

ma = MovingAverage(3)
# ma.add_value(10)
# ma.add_value(20)
# ma.add_value(30)
print(ma.get_average())  # Output: 20.0
ma.add_value(40)
print(ma.get_average())  # Output: 30.0