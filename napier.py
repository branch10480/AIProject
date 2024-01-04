import numpy as np
import matplotlib.pyplot as plt


def main():
    print_napier()
    # draw()
    draw2()


def draw():
    x = np.linspace(-2, 2)
    e = np.e
    y1 = 2 ** x
    y2 = 3 ** x
    y3 = e ** x

    plt.xlabel("x", size=14)
    plt.ylabel("y", size=14)

    plt.title("My Graph", size=20)

    plt.plot(x, y1, label="2^x")
    plt.plot(x, y2, label="3^x")
    plt.plot(x, y3, label="e^x")

    plt.grid()
    plt.legend()
    plt.show()


def draw2():
    x = np.linspace(-2, 2)
    e = np.e
    dx = 0.01

    y_e = e**x
    y_de = (e**(x+dx) - e**x) / dx

    plt.xlabel("x", size=14)
    plt.ylabel("y", size=14)

    plt.title("My Graph", size=20)

    plt.plot(x, y_e, label="e^x")
    plt.plot(x, y_de, label="de")

    plt.grid()
    plt.legend()
    plt.show()

    # ネイピア数のべき乗は微分してもほぼ同一となるのでAIの分野ではよく使われる


def print_napier():
    print(np.e)


if __name__ == "__main__":
    main()
