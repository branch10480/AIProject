import matplotlib.pyplot as plt
import numpy as np


def main():
    # draw_graph1()
    draw_graph2()


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


if __name__ == "__main__":
    main()
