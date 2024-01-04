import numpy as np


class Neuron:
    def __init__(self):
        self.input_sum = 0.0
        self.output = 0.0

    def reset(self):
        self.input_sum = 0.0
        self.output = 0.0

    def set_input(self, inp):
        self.input_sum += inp
        print(self.input_sum)

    def get_output(self):
        self.output = sigmoid(self.input_sum)
        return self.output


class NeuralNetwork:
    def __init__(self):
        self.neuron = Neuron()
        self.w = [1.5, 0.75, -1.0]
        # 神経の興奮のしやすさ これを入力*重みの総和に足し合わせる
        # self.bias = 1.0
        self.bias = -1.0

    # 実行
    def commit(self, input_data):
        self.neuron.set_input(input_data[0] * self.w[0])
        self.neuron.set_input(input_data[1] * self.w[1])
        self.neuron.set_input(input_data[2] * self.w[2])
        # バイアスを足し合わせる
        self.neuron.set_input(self.bias)
        return self.neuron.get_output()


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))  # エクスポネンシャル (exp) 関数: eのべき乗
