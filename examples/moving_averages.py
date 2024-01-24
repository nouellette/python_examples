import matplotlib.pyplot as plt
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.stream = deque()
        self.sum = 0

    def add(self, val):
        self.stream.append(val)
        self.sum += val
        if len(self.stream) > self.size:
            self.sum -= self.stream.popleft()
        return self.sum / len(self.stream)

def plot_data_with_moving_average(data_points, window_size):
    moving_average = MovingAverage(window_size)
    moving_averages = [moving_average.add(val) for val in data_points]

    plt.figure(figsize=(10, 6))
    plt.plot(data_points, label='Data Points', marker='o')  # Data points
    plt.plot(moving_averages, label='Moving Average', marker='x')  # Moving averages
    plt.title('Data Points and Moving Average (Window Size = {0})'.format(window_size))
    plt.xlabel('Data Point Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

data_points = [2, 4, 3, 7, 3, 6, 7, 9, 9, 10]
window_size = len(data_points)
plot_data_with_moving_average(data_points, window_size)