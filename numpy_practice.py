import numpy as np


def main():
    list = [1, 2, 3, 4, 5]
    numpy_list = np.array(list)
    print(numpy_list)
    print(len(numpy_list))

    divided = np.linspace(0, 10)  # 0から10までを50分割する
    print(divided)


if __name__ == "__main__":
    main()
