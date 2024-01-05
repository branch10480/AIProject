from neuron import Neuron
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np


# 入力層、中間層、出力層の3層構造にする

def main():
    data = datasets.load_iris().data
    sl_data = data[:100, 0]  # Sepal Length (Setosa, Versicolor)
    sw_data = data[:100, 1]  # Sepal Width (Setosa, Versicolor)

    # 平均値を0にする
    sl_avg = np.average(sl_data)   # 平均値
    sl_data -= sl_avg                   # 平均値を引く
    sw_avg = np.average(sw_data)
    sw_data -= sw_avg

    # 入力をリストに格納する
    input_data = []
    for i in range(len(sl_data)):
        input_data.append((sl_data[i], sw_data[i]))

    nw = NeuralNetwork()

    # 実行
    st_predicted = [[], []]  # Setosa
    vc_predicted = [[], []]  # Versicolor
    for data in input_data:
        if nw.commit(data) < 0.5:
            st_predicted[0].append(data[0] + sl_avg)
            st_predicted[1].append(data[1] + sw_avg)
        else:
            vc_predicted[0].append(data[0] + sl_avg)
            vc_predicted[1].append(data[1] + sw_avg)

    plt.title("Classify")

    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")

    plt.scatter(st_predicted[0], st_predicted[1], label="Setosa")
    plt.scatter(vc_predicted[0], vc_predicted[1], label="Versicolor")

    # legend() を実行する位置はグラフのプロットを行ったあとにしないと表示されない
    plt.legend()

    plt.show()


class NeuralNetwork:
    def __init__(self):
        # 重み
        self.w_im = [[4.0, 4.0], [4.0, 4.0], [4.0, 4.0]]  # 入力2, ニューロン数3
        self.w_mo = [[1.0, -1.0, 1.0]]                    # 入力3, ニューロン数1

        # バイアス
        self.b_m = [3.0, 0.0, -3.0]           # ニューロン数3
        self.b_o = [-0.5]                     # ニューロン数1

        # 各層の宣言
        self.input_layer = [0.0, 0.0]                        # 入力層
        self.middle_layer = [Neuron(), Neuron(), Neuron()]   # 中間層
        self.output_layer = [Neuron()]                       # 出力層

    def commit(self, input_data):
        # 各層のリセット
        self.input_layer[0] = input_data[0]  # 入力層は値を受け取るのみ
        self.input_layer[1] = input_data[1]
        self.middle_layer[0].reset()
        self.middle_layer[1].reset()
        self.middle_layer[2].reset()
        self.output_layer[0].reset()

        # 入力層→中間層
        self.middle_layer[0].set_input(self.input_layer[0] * self.w_im[0][0])
        self.middle_layer[0].set_input(self.input_layer[1] * self.w_im[0][1])
        self.middle_layer[0].set_input(self.b_m[0])

        self.middle_layer[1].set_input(self.input_layer[0] * self.w_im[1][0])
        self.middle_layer[1].set_input(self.input_layer[1] * self.w_im[1][1])
        self.middle_layer[1].set_input(self.b_m[1])

        self.middle_layer[2].set_input(self.input_layer[0] * self.w_im[2][0])
        self.middle_layer[2].set_input(self.input_layer[1] * self.w_im[2][1])
        self.middle_layer[2].set_input(self.b_m[2])

        # 中間層→出力層
        self.output_layer[0].set_input(self.middle_layer[0].get_output() * self.w_mo[0][0])
        self.output_layer[0].set_input(self.middle_layer[1].get_output() * self.w_mo[0][1])
        self.output_layer[0].set_input(self.middle_layer[2].get_output() * self.w_mo[0][2])
        self.output_layer[0].set_input(self.b_o[0])

        return self.output_layer[0].get_output()


if __name__ == '__main__':
    main()
