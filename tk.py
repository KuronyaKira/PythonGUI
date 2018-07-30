import tkinter as tk
import tkinter.font as font

def pushed(self):
 self["text"] = '%sさん、こんにちは。'%textbox.get()

# コメント出力
print('ハラショー')

# メインウィンドウ作成
root = tk.Tk()
#メインウィンドウのタイトルを変更
root.title("GUI テスト")
#メインウィンドウを640x480にする
root.geometry("640x480")

# my_fontというフォントオブジェクトを新規に作成
my_font = font.Font(root,family="ゆたぽん（コーディング）",size=20)

#ラベルを追加
label = tk.Label(root, text="名前を教えてね。",font=my_font)
#表示
label.grid()

#テキストボックスを追加
textbox = tk.Entry(root, text="",font=my_font)
#表示
textbox.grid()


#ボタンを追加、表示
button = tk.Button(root, text="決定", command= lambda : pushed(label),font=my_font)
button.grid()

#rootを表示し無限ループ
root.mainloop()