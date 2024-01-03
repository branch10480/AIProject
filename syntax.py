def main():
    print("Hello World!")

    # 変数定義
    a = 123
    print(a)

    # 割り算
    print(10 / 3)   # 少数
    print(10 // 3)  # 整数

    # Bool
    true = True
    false = False

    # if文
    if false:
        print("true")
    else:
        print("false")

    # list
    list = [1, 2, 3, 4, 5]
    # 要素数の取得はlen関数
    list.append(list[len(list)-1] + 1)
    print(list)

    # tuple
    # 要素の変更ができない
    tuple = (1, 2, 3, 4, 5)
    print(tuple)

    # 辞書
    dict = {"one": 1, "two": 2, "three": 3}
    print(dict)

    print("For文 - list")
    for item in list:
        print(item)

    # dictのforとjoin
    print("For文 - dict")
    print(", ".join(dict.keys()))
    for key in dict:
        print(dict[key])

    # range
    print("For文 - range")
    for i in range(0, 5):
        print(i)

    odd = []
    for i in range(0, 10):
        if i % 2 != 0:
            odd.append(i)
    print("奇数")
    print(odd)


# importしただけでは実行されないようにするためにこの判定を書く
# このファイルが直接実行された場合は __name__ に __main__ が入る
if __name__ == "__main__":
    main()
