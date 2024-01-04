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

    say_hello()
    say_hello_to("Taro")
    print(added(1))

    # クラスの利用
    calc = Calc(1)
    calc.add(2)
    print(calc.get())

    # with構文を用いたファイルの書き込み
    greetings = "Good morning!\nGood night!"
    with open("greeting.txt", "w") as f:
        f.write(greetings)

    # with構文を用いたファイルの読み込み
    with open("greeting.txt", "r") as f:
        print(f.read())

    # callメソッドの呼び出し
    calc("Callメソッドの呼び出し")

    # アンパック
    numbers = [1, 2, 3]
    a, b, c = numbers
    print(a)
    print(b)
    print(c)

    # アンパック（*）
    numbers = [1, 2, 3, 4, 5]
    a, b, *c = numbers
    print(a)
    print(b)
    print(c)

    # アンパック（**）
    def greet(first_name, last_name):
        print(f"Hi {first_name} {last_name}!")

    person = {"first_name": "Taro", "last_name": "Yamada"}
    greet(**person)


# 関数定義
def say_hello():
    print("Hello!")


def say_hello_to(name):
    print("Hello " + name + "!")


def added(num):
    return num + 1


class Calc:
    def __init__(self, num):
        self.num = num

    def __call__(self, *args, **kwargs):
        print(", ".join(args))

    def add(self, num):
        self.num += num

    def sub(self, num):
        self.num -= num

    def get(self):
        return self.num


# importしただけでは実行されないようにするためにこの判定を書く
# このファイルが直接実行された場合は __name__ に __main__ が入る
if __name__ == "__main__":
    main()
