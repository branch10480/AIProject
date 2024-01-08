from sklearn import svm, datasets, metrics
from sklearn.model_selection import train_test_split


def main():
    wines = datasets.load_wine()
    print(wines.data)
    print(wines.data.shape)

    clf = svm.SVC()
    x_train, x_test, y_train, y_test = train_test_split(wines.data, wines.target)
    clf.fit(x_train, y_train)

    y_test_pred = clf.predict(x_test)

    print(y_test[-10:])
    print(y_test_pred[-10:])

    print(metrics.classification_report(y_test, y_test_pred))
    print(metrics.confusion_matrix(y_test, y_test_pred))


if __name__ == '__main__':
    main()
