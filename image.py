import tkinter as tk
import tkinter.font as font

nicoSW = False


def pushed(self):
    self["text"] = '%sさん、こんにちは。' % textbox.get()


def pushed2(self):
    global nicoSW

    if nicoSW == False:
        nicoSW = True
        self["text"] = 'にこでーす。'
    else:
        nicoSW = False
        self["text"] = ''


# コメント出力
print('ハラショー')

# メインウィンドウ作成
root = tk.Tk()
# メインウィンドウのタイトルを変更
root.title("GUI テスト")
# メインウィンドウを640x480にする
root.geometry("640x480")

# my_fontというフォントオブジェクトを新規に作成
my_font = font.Font(root, family="ゆたぽん（コーディング）", size=20)

# ラベルを追加
label = tk.Label(root, text="名前を教えてね。", font=my_font)
# 表示
label.grid()

# テキストボックスを追加
textbox = tk.Entry(root, text="", font=my_font)
# 表示
textbox.grid()

# ボタンを追加、表示
button = tk.Button(
    root, text="決定", command=lambda: pushed(label), font=my_font)
button.grid()

# 画像表示場所の追加
img = tk.PhotoImage(file='titlenico.png')
button2 = tk.Button(
    root,
    command=lambda: pushed2(label2),
    width=300,
    height=300,
    relief=tk.RIDGE,
    bd=0,
    image=img)
button2.grid()

# ラベル2を追加
label2 = tk.Label(root, text="", font=my_font)
# 表示
label2.grid()

# rootを表示し無限ループ
root.mainloop()
