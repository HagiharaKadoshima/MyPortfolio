import datetime
import tkinter as tk
import twitter

#ボタンがクリックされたら実行
def button_click():

    # boxからテキストを取得してcontentsに代入
    contents = contents_box.get("1.0", 'end')
    twitter.tweet(contents)

#ウインドウの作成
root = tk.Tk()
root.title("Python GUI")
root.geometry("650x450")

#入力欄の作成
title_box = tk.Entry(width=45)
title_box.place(x=70, y=20)

#ラベルの作成
title_label = tk.Label(text="タイトル")
title_label.place(x=10, y=20)

#入力欄の作成
contents_box = tk.Text(insertbackground="#fff",height=25, width=70)
contents_box.place(x=70, y=50)

#ラベルの作成
contents_label = tk.Label(text="内容")
contents_label.place(x=10, y=50)

#ボタンの作成
button = tk.Button(text="実行ボタン",command=button_click)
button.place(x=500, y=380)

#ウインドウの描画
root.mainloop()




