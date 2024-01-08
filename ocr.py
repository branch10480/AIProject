import matplotlib.pyplot as plt
from sklearn import datasets, svm


def main():
    # 数字画像データの読み込み
    digits = datasets.load_digits()

    # 要素は画像の明るさを表す 0 から 15 までの値 0が明るく、15が暗い
    print("--- 画像データ ---")
    # 全体で3次元配列、8x8の2次元配列が1797個
    print(digits.images[0])
    print(digits.images.shape)
    print("--- 1次元画像データ ---")
    # 全体で2次元配列、64個の1次元配列が1797個 機械学習ではこの形の方が扱いやすい
    print(digits.data[0])
    print(digits.data.shape)
    print("--- ラベル ---")
    print(digits.target)
    print(digits.target.shape)

    # 画像と正解値の表示
    images = digits.images
    labels = digits.target
    for i in range(10):
        # subplotで画像を複数枚並べて表示することができる
        plt.subplot(2, 5, i + 1)    # 2行5列のグラフのi+1番目
        plt.imshow(images[i], cmap="Greys")     # cmap="Greys"でグレースケールにする cmapはカラーマップの略
        plt.axis("off")
        plt.title("Label: " + str(labels[i]))
    plt.show()

    # 手書き文字の分類
    # データ全体を train_test_split を使って訓練データとテストデータに分ける


def train_test_split(data):
    return


'''
--- 画像データ ---
[[ 0.  0.  5. 13.  9.  1.  0.  0.]
 [ 0.  0. 13. 15. 10. 15.  5.  0.]
 [ 0.  3. 15.  2.  0. 11.  8.  0.]
 [ 0.  4. 12.  0.  0.  8.  8.  0.]
 [ 0.  5.  8.  0.  0.  9.  8.  0.]
 [ 0.  4. 11.  0.  1. 12.  7.  0.]
 [ 0.  2. 14.  5. 10. 12.  0.  0.]
 [ 0.  0.  6. 13. 10.  0.  0.  0.]]
(1797, 8, 8)
--- 1次元画像データ ---
[ 0.  0.  5. 13.  9.  1.  0.  0.  0.  0. 13. 15. 10. 15.  5.  0.  0.  3.
 15.  2.  0. 11.  8.  0.  0.  4. 12.  0.  0.  8.  8.  0.  0.  5.  8.  0.
  0.  9.  8.  0.  0.  4. 11.  0.  1. 12.  7.  0.  0.  2. 14.  5. 10. 12.
  0.  0.  0.  0.  6. 13. 10.  0.  0.  0.]
(1797, 64)
--- ラベル ---
[0 1 2 ... 8 9 8]
(1797,)
'''

if __name__ == "__main__":
    main()
