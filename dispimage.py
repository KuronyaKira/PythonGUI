import tkinter as tk
import tkinter.font as font
from PIL import ImageTk as itk

nicoSW = False


def pushed(self):
    img = itk.PhotoImage(file='images/1.jpg')
    self["image"] = img


# コメント出力
print('ハラショー')

# メインウィンドウ作成
root = tk.Tk()
# メインウィンドウのタイトルを変更
root.title("GUI テスト")
# メインウィンドウを640x480にする
root.geometry("640x480")

# 画像表示場所の追加
img = itk.PhotoImage(file='images/1.jpg')
canvas = tk.Canvas(
    root,
    width=300,
    height=300)
canvas.create_image(150, 150, image=img)
canvas.grid()


# rootを表示し無限ループ
root.mainloop()
