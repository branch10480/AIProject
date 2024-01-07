from sklearn import datasets, svm   # svm: サポートベクターマシン


def main():
    iris = datasets.load_iris()
    # print(iris.data, iris.target)   # 品種を表すラベル（0: Setosa, 1: Versicolor, 2: Versinica）が返ってくる

    # インスタンス、数学的にはモデル
    clf = svm.SVC()     # サポートベクターマシン SVC: Support Vector Classification
    clf.fit(iris.data, iris.target)     # 学習（訓練）

    # 品種の判定（Sepal Length, Sepal Width, Petal Length, Petal Width）
    print(clf.predict([[5.1, 3.5, 1.4, 0.1], [6.5, 2.5, 4.4, 1.4], [5.9, 3.0, 6.2, 2.0]]))


if __name__ == '__main__':
    main()
