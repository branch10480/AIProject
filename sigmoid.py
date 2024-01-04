import numpy as np
import matplotlib.pyplot as plt


def main():
    # draw_graph()
    draw_graph2()


def draw_graph():
    x = np.linspace(-5, 5)
    e = np.e

    y = sigmoid(x)

    plt.xlabel("x", size=14)
    plt.ylabel("y", size=14)

    plt.title("My Graph", size=20)

    plt.plot(x, y, label="sigmoid")

    plt.grid()
    plt.legend()
    plt.show()


def draw_graph2():
    x = np.linspace(-8, 8)
    e = np.e
    dx = 0.1

    y = sigmoid(x)
    y2 = (sigmoid(x + dx) - sigmoid(x)) / dx
    y3 = df_sigmoid(x)

    plt.xlabel("x", size=14)
    plt.ylabel("y", size=14)

    plt.title("My Graph", size=20)

    plt.plot(x, y, label="sigmoid")
    plt.plot(x, y2, label="de")
    plt.plot(x, y3, label="df_sigmoid")

    plt.grid()
    plt.legend()
    plt.show()


# シグモイド関数: 0~1の値をとる
def sigmoid(x):
    return 1 / (1 + np.e ** (-x))


# シグモイド関数の微分
def df_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


if __name__ == "__main__":
    main()
