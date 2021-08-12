import datetime
import os
import tkinter as tk
from tkinter import messagebox
import twittertest
import LINE
import tkinter.filedialog
from PIL import Image, ImageTk
from sys import version_info

def ConvertText(title, content):
    TextFormat = title + "\n\n" + content
    return TextFormat

#ボタンがクリックされたら実行
def button_click():
    if contents_box.get("1.0", 'end-1c') == "":
        tk.messagebox.showwarning("警告", "内容にデータが入力されていません")
    elif title_box.get() == "":
        tk.messagebox.showwarning("警告", "タイトルにデータが入力されていません")
    else:
        contents = contents_box.get("1.0", 'end-1c')
        title = title_box.get()
        text = ConvertText(title, contents)
        LINE.sendmessage(text)
        twittertest.tweet(text, *file_names)

    # boxからテキストを取得してcontentsに代入
    #contents = contents_box.get("1.0", 'end')
    #twitter.tweet(contents)


def imgset(number):

    #messagebox("imgset_file_names[number]", file_names[number])
    #画像処理
    img1 = Image.open(file_names[number])
    width = 200  # 画像のサイズ
    height = round(img1.height * width / img1.width)
    im_resize = img1.resize(size=(width, height))
    im_resize.thumbnail((500, 500), Image.ANTIALIAS)
    im_resize = ImageTk.PhotoImage(im_resize)  # 表示するイメージを用意

    # キャンバス上にイメージを配置
    canvas[number].delete("all")
    canvas[number].create_image(
        0,  # x座標
        0,  # y座標
        image=im_resize,  # 配置するイメージオブジェクトを指定
        tag="illust",  # タグで引数を追加する。
        anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
    )

    root.mainloop()


def file_dialog(number):

    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file_names[number] = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    imgset(number)

#変数定義
file_names = ["", ""]

#ウインドウの作成
root = tk.Tk()
root.title("投稿アプリ")
root.geometry("600x700")

#入力欄の作成
title_box = tk.Entry(width=45)
title_box.place(x=70, y=20)

#ラベルの作成
title_label = tk.Label(text="タイトル")
title_label.place(x=10, y=20)

#入力欄の作成
contents_box = tk.Text(insertbackground="#fff", height=25, width=70)
contents_box.place(x=70, y=50)

#ラベルの作成
contents_label = tk.Label(text="内容")
contents_label.place(x=10, y=50)

#画像追加の作成
ImgButton1 = tk.Button(text="画像選択", command=lambda: file_dialog(0))
ImgButton1.place(x=35, y=390)

#画像追加の作成
ImgButton2 = tk.Button(text="画像選択", command=lambda: file_dialog(1))
ImgButton2.place(x=260, y=390)

#投稿ボタンの作成
PostButton = tk.Button(text="投稿", height=12, width=7, font=20, command=button_click)
PostButton["relief"] = "groove"
PostButton.place(x=485, y=400)

#描画場所
canvas1 = tk.Canvas(
    root,  # 親要素をメインウィンドウに設定
    width=200,  # 幅を設定
    height=200,  # 高さを設定
    relief=tk.RIDGE,  # 枠線を表示
    borderwidth=3     # 枠線の幅を設定
)

#描画場所
canvas2 = tk.Canvas(
    root,  # 親要素をメインウィンドウに設定
    width=200,  # 幅を設定
    height=200,  # 高さを設定
    relief=tk.RIDGE,  # 枠線を表示
    borderwidth=3     # 枠線の幅を設定
)

canvas = [canvas1, canvas2]

canvas1.place(x=30, y=430)  # メインウィンドウ上に配置
canvas2.place(x=260, y=430)  # メインウィンドウ上に配置

#ウインドウの描画
root.mainloop()
