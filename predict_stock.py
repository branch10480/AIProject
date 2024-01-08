import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split


# 株価分析


def main():
    with open('stock_price.txt', 'r') as f:
        stock_file_data = f.read().split()  # ファイルの読み込み
        stock_data = list(map(lambda x: float(x), stock_file_data))

    # データの確認
    print("株価", stock_data)
    print("Shape:", np.array(stock_data).shape)

    # 株価の変化率に変換する
    ratio_data = []
    for i in range(1, len(stock_data)):
        data = (stock_data[i] - stock_data[i - 1]) / stock_data[i - 1]
        ratio_data.append(data)
    print("株価の変化率:", ratio_data)
    print("株価の変化率データの要素数:", len(ratio_data))

    # 前日までの4連続の変化率のデータ
    successive_data = []
    answers = []            # 正解値 1:上昇, 0:下降
    for i in range(4, len(ratio_data)):
        # successive_data.append((ratio_data[i - 4], ratio_data[i - 3], ratio_data[i - 2], ratio_data[i - 1]))
        # スライスを使えば短く書ける
        successive_data.append(tuple(ratio_data[i-4:i]))
        if ratio_data[i] > 0:
            answers.append(1)
        else:
            answers.append(0)

    # print("4連続の変化率のデータ:", successive_data)
    # print("回答:", answers)

    # 分類器を作成
    clf = svm.SVC()     # サポートベクターマシン
    x_train, x_test, y_train, y_test = train_test_split(successive_data, answers, shuffle=False)    # シャッフルはしない
    clf.fit(x_train, y_train)

    # 予測
    y_test_pred = clf.predict(x_test)

    # 予測結果を表示 - 末尾から10個
    print("予測結果:", y_test_pred[-10:])   # list
    print("正解:", y_test[-10:])           # numpy の配列

    # 正解率を表示
    correct = 0.0
    wrong = 0.0

    for i in range(len(y_test)):
        if y_test[i] == y_test_pred[i]:
            correct += 1
        else:
            wrong += 1

    print("正解率:" + str(correct / (correct + wrong) * 100) + "%")


if __name__ == '__main__':
    main()
