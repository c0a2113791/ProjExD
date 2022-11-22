import random
import time
moijsu = 10 #対象文字数
kesson = 2 #欠損文字数
playtime = 2 #最大繰り返し回数

def shutudai(alphabet):#出題するアルファベット10文字、欠損後の文字を表示する
    all_chars = random.sample(alphabet,moijsu)
    print("対象文字:")
    for c in all_chars:
        print(c, end = " ")
    print()

    abs_chars = random.sample(all_chars,kesson)
    #print("欠損文字（デバッグ用）")
    #for c in abs_chars:
    #    print(c, end = " ")
    #print()

    print("表示文字")
    for c in all_chars:
        if c not in abs_chars:
            print(c,end = " ")
    print()
    return abs_chars

def kaitou(abs_char):#回答の正解、不正解を判定する。
    num = int(input("欠損文字はいくつあるでしょうか？:"))
    if num != kesson:
        print("不正解です")
    else:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(num):
            ans = input(f"{i + 1}1つ目の文字を入力してください:")
            if ans not in abs_char:
                print("不正解です")
                return False
            else:
                abs_char.remove(ans)
        print("全部正解です")
        return True


if __name__ == "__main__":
    st = time.time()
    alphabet = [chr(i + 65) for i in range (moijsu)]
    print(alphabet)
    for _ in range(playtime):
        abs_char = shutudai(alphabet)
        ret = kaitou(abs_char)
        if ret:
            
            break

        else:

            print("-" * 20)
    
    ed = time.time()
    print(f"所要時間:{(ed-st):.2f}秒")