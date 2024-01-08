import numpy as np


def main():
    # sample1()
    sample2()


def sample1():
    a = np.array([[0, 1, 2, 3],     # 行列 npのarrayを使う
                  [1, 2, 3, 4],
                  [2, 3, 4, 5]])
    print(a)


def sample2():
    a = np.array([[0, 1, 2],    # 行列A
                  [1, 2, 3]])
    b = np.array([[2, 1],       # 行列B
                  [2, 1],
                  [2, 1]])

    # 行列積ABを計算するにはAの行とBの列数が一致していなければならない
    # 行列積の計算はnumpyのdot関数を使う
    result = np.dot(a, b)

    print(result)


if __name__ == '__main__':
    main()
