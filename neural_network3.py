from neuron import Neuron
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from neuron import df_sigmoid
import random


# 入力層、中間層、出力層の3層構造にする

def main():
    iris = datasets.load_iris()
    data = iris.data
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
        correct = iris.target[i]
        input_data.append((sl_data[i], sw_data[i], correct))

    nw = NeuralNetwork()

    # 学習と結果の表示
    for i in range(0, 32):
        random.shuffle(input_data)  # データをシャッフル
        for data in input_data:
            nw.commit(data[:2])        # 順伝播
            nw.train(data[2])          # 逆伝播
        if i+1 in [1, 2, 4, 8, 16, 32]:
            draw_graph(i+1, nw, sl_avg, sw_avg, input_data)

    # 比較用に元の分類を散布図で表示
    st_data = iris.data[:50]  # Sepal Length (Setosa)
    vc_data = iris.data[50:100]  # Sepal Length (Versicolor)
    plt.scatter(st_data[:, 0], st_data[:, 1], label="Setosa")
    plt.scatter(vc_data[:, 0], vc_data[:, 1], label="Versicolor")
    plt.legend()

    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Original")
    plt.show()


def draw_graph(epoch, nw, sl_avg, sw_avg, input_data):
    print("Epoch:", epoch)
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

    plt.title("Classify - Epoch: " + str(epoch))

    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")

    # 分類結果をグラフ表示
    plt.scatter(st_predicted[0], st_predicted[1], label="Setosa")
    plt.scatter(vc_predicted[0], vc_predicted[1], label="Versicolor")

    # legend() を実行する位置はグラフのプロットを行ったあとにしないと表示されない
    plt.legend()

    plt.show()



class NeuralNetwork:
    def __init__(self):
        # 重み
        self.w_im = [[4.0, 4.0], [4.0, 4.0]]  # 入力2, ニューロン数2
        self.w_mo = [[1.0, -1.0]]        # 入力3, ニューロン数1

        # バイアス
        self.b_m = [2.0, -2.0]           # ニューロン数3
        self.b_o = [-0.5]                     # ニューロン数1

        # 各層の宣言
        self.input_layer = [0.0, 0.0]                        # 入力層
        self.middle_layer = [Neuron(), Neuron()]             # 中間層
        self.output_layer = [Neuron()]                       # 出力層

    def commit(self, input_data):
        # 各層のリセット
        self.input_layer[0] = input_data[0]  # 入力層は値を受け取るのみ
        self.input_layer[1] = input_data[1]
        self.middle_layer[0].reset()
        self.middle_layer[1].reset()
        self.output_layer[0].reset()

        # 入力層→中間層
        self.middle_layer[0].set_input(self.input_layer[0] * self.w_im[0][0])
        self.middle_layer[0].set_input(self.input_layer[1] * self.w_im[0][1])
        self.middle_layer[0].set_input(self.b_m[0])

        self.middle_layer[1].set_input(self.input_layer[0] * self.w_im[1][0])
        self.middle_layer[1].set_input(self.input_layer[1] * self.w_im[1][1])
        self.middle_layer[1].set_input(self.b_m[1])

        # 中間層→出力層
        self.output_layer[0].set_input(self.middle_layer[0].get_output() * self.w_mo[0][0])
        self.output_layer[0].set_input(self.middle_layer[1].get_output() * self.w_mo[0][1])
        self.output_layer[0].set_input(self.b_o[0])

        return self.output_layer[0].get_output()


    def train(self, correct):
        # 学習係数
        k = 0.3

        # 出力
        output_o = self.output_layer[0].get_output()
        output_m0 = self.middle_layer[0].get_output()
        output_m1 = self.middle_layer[1].get_output()

        # δ
        delta_o = (output_o - correct) * df_sigmoid(output_o)
        delta_m0 = delta_o * self.w_mo[0][0] * df_sigmoid(output_m0)
        delta_m1 = delta_o * self.w_mo[0][1] * df_sigmoid(output_m1)

        # パラメータの更新
        # 出力層
        self.b_o[0] += -k * delta_o
        self.w_mo[0][0] += -k * delta_o * output_m0
        self.w_mo[0][1] += -k * delta_o * output_m1
        # 中間層
        self.b_m[0] += -k * delta_m0
        self.b_m[1] += -k * delta_m1
        self.w_im[0][0] += -k * delta_m0 * self.input_layer[0]
        self.w_im[0][1] += -k * delta_m0 * self.input_layer[1]
        self.w_im[1][0] += -k * delta_m1 * self.input_layer[0]
        self.w_im[1][1] += -k * delta_m1 * self.input_layer[1]


if __name__ == '__main__':
    main()
