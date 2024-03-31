import tkinter as tk

def change_label_text():
    label.config(text="ボタンがクリックされました！")

window = tk.Tk()
window.title("シンプルなGUIアプリ")

label = tk.Label(window, text="ラベル")
label.pack()

button = tk.Button(window, text="クリックしてください", command=change_label_text)
button.pack()

window.mainloop()