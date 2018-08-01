import tkinter as tk
import tkinter.font as font


def pushed(self):
    self["image"] = tk.PhotoImage(file='images/1.png')


# メインウィンドウ作成
root = tk.Tk()
#メインウィンドウのタイトルを変更
root.title("GUI テスト")
#メインウィンドウを640x480にする
root.geometry("640x480")

img = tk.PhotoImage(file='images/1.png')
button1 = tk.Button(
    root,
    command=lambda: pushed(canvas),
    width=300,
    height=300,
    relief=tk.RIDGE,
    bd=0,
    image=img)
button1.grid()

img = tk.PhotoImage(file='images/2.jpg')
button2 = tk.Button(
    root,
    command=lambda: pushed(canvas),
    width=300,
    height=300,
    relief=tk.RIDGE,
    bd=0,
    image=img)
button2.grid()

canvas = tk.Canvas(
    root,  # 親要素をメインウィンドウに設定
    width=500,  # 幅を設定
    height=500,  # 高さを設定
)
canvas.place(x=370, y=0)  # メインウィンドウ上に配置

canvas.create_image(  # キャンバス上にイメージを配置
    0,  # x座標
    0,  # y座標
    anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
)

# rootを表示し無限ループ
root.mainloop()
