import numpy as np
import sklearn.datasets as datasets
import matplotlib.pyplot as plt


def main():
    # Irisデータの読み込み
    iris = datasets.load_iris()

    # 各花のサイズ
    iris_data = iris.data

    # 散布図で表示
    st_data = iris_data[:50]  # Setosa
    vc_data = iris_data[50:100]  # Versicolor
    vn_data = iris_data[100:150]  # Virginica

    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.title("Iris Sepal")
    plt.scatter(st_data[:, 0], st_data[:, 1], label="Setosa")       # Sepal length, Sepal width
    plt.scatter(vc_data[:, 0], vc_data[:, 1], label="Versicolor")
    plt.scatter(vn_data[:, 0], vn_data[:, 1], label="Virginica")
    plt.legend()
    plt.show()

    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Iris Petal")
    plt.scatter(st_data[:, 2], st_data[:, 3], label="Setosa")       # Petal length, Peta width
    plt.scatter(vc_data[:, 2], vc_data[:, 3], label="Versicolor")
    plt.scatter(vn_data[:, 2], vn_data[:, 3], label="Virginica")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
