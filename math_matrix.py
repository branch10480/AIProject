import numpy as np


def main():
    # sample1()
    # sample2()
    # sample3()
    sample4()


def sample1():
    a = np.array([[0, 1, 2, 3],  # 行列 npのarrayを使う
                  [1, 2, 3, 4],
                  [2, 3, 4, 5]])
    print(a)


def sample2():
    a = np.array([[0, 1, 2],  # 行列A
                  [1, 2, 3]])
    b = np.array([[2, 1],  # 行列B
                  [2, 1],
                  [2, 1]])

    # 行列積ABを計算するにはAの行とBの列数が一致していなければならない
    # 行列積の計算はnumpyのdot関数を使う
    result = np.dot(a, b)

    print(result)


def sample3():
    # 入力: 3 ニューロン: 2
    x = np.array([[0, 0.5, 1.0]])  # 入力
    w = np.array([[-1, 1],  # 重み
                  [1, -1],
                  [-1, 1]])
    print(np.dot(x, w))  # 入力と重みの積の総和


def sample4():
    a = np.array([[0, 1, 2],  # 2*3の行列
                  [4, 5, 6]])
    # 転置させる前
    print("転置させる前")
    print(a)

    # 転置させる .T
    print("転置させた後")
    print(a.T)

    print("--------")

    b = np.array([[0, 1, 2],  # 2*3の行列 このままだと行列積 a*b ができない
                  [4, 5, 6]])

    print(np.dot(a, b.T))  # bを転置して行列積を計算する


if __name__ == '__main__':
    main()
