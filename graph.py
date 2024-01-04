import matplotlib.pyplot as plt
import numpy as np


def main():
    # draw_graph1()
    # draw_graph2()
    draw_graph3()


def draw_graph1():
    x = np.linspace(-5, 5)
    y = 2*x+1

    plt.plot(x, y)
    plt.show()


def draw_graph2():
    x = np.linspace(-3, 3)
    y1 = 1.5*x
    y2 = -2*x+1

    plt.xlabel("x", size=14)
    plt.ylabel("y", size=14)

    plt.title("My Graph", size=20)

    plt.grid()

    plt.plot(x, y1, label="y1")
    plt.plot(x, y2, label="y2", linestyle="dashed")

    plt.legend()

    plt.show()


def draw_graph3():
    x = np.linspace(-4, 4)
    y1 = 2*x+1
    y2 = x**2-4
    y3 = 0.5*x**3-6*x

    plt.xlabel("x", size=14)
    plt.ylabel("y", size=14)

    plt.title("My Graph", size=20)

    plt.grid()

    plt.plot(x, y1, label="y1")
    plt.plot(x, y2, label="y2")
    plt.plot(x, y3, label="y3")

    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
