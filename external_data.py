import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from neuron import Neuron
from neuron import NeuralNetwork


def main():
    original()
    classify()


def original():
    # データの読み込み
    iris = datasets.load_iris()
    data = iris.data

    # データの表示
    print("Data")
    print(data)

    # 150行4列のデータ
    print("Data - Shape")
    print(data.shape)

    st_data = data[:50]  # Setosa 0~49
    vc_data = data[50:100]  # Versicolor 50~99

    plt.title("Original")

    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")

    plt.scatter(st_data[:, 0], st_data[:, 1], label="Setosa")
    plt.scatter(vc_data[:, 0], vc_data[:, 1], label="Versicolor")

    plt.show()


def classify():
    data = datasets.load_iris().data
    # データをごちゃまぜにする
    sl_data = data[:100, 0]  # Sepal Length (Setosa, Versicolor)
    sw_data = data[:100, 1]  # Sepal Width (Setosa, Versicolor)

    # 平均値を0にする
    sl_avg = np.average(sl_data)  # 平均値
    sl_data -= sl_avg  # 平均値を引く
    sw_avg = np.average(sw_data)
    sw_data -= sw_avg

    # 入力をリストに格納する
    input_data = []
    for i in range(100):  # 0~99
        input_data.append((sl_data[i], sw_data[i]))

    nw = MyNeuralNetwork()

    # 実行
    st_predicted = [[], []]  # Setosa
    vc_predicted = [[], []]  # Versicolor
    for data in input_data:
        if nw.commit(data) < 0.5:
            # 平均値を足してもとの長さにする
            st_predicted[0].append(data[0] + sl_avg)
            st_predicted[1].append(data[1] + sw_avg)
        else:
            # 平均値を足してもとの長さにする
            vc_predicted[0].append(data[0] + sl_avg)
            vc_predicted[1].append(data[1] + sw_avg)

    plt.title("Classify")

    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")

    plt.scatter(st_predicted[0], st_predicted[1], label="Setosa")
    plt.scatter(vc_predicted[0], vc_predicted[1], label="Versicolor")

    plt.show()


class MyNeuralNetwork(NeuralNetwork):
    def __init__(self):
        self.neuron = Neuron()
        self.w = [0.5, -0.2]
        self.bias = 0.06

    def commit(self, input_data):
        self.neuron.reset()

        self.neuron.set_input(input_data[0] * self.w[0])
        self.neuron.set_input(input_data[1] * self.w[1])
        self.neuron.set_input(self.bias)

        return self.neuron.get_output()


if __name__ == '__main__':
    main()
