import tkinter as tk
import spam as sp

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def get_result():
    x1 = entry1.get()
    result=sp.detect_spam(x1)

    label1 = tk.Label(root, text=result)
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='Get Result', command=get_result)
canvas1.create_window(200, 180, window=button1)

if __name__ == "__main__":
    sp.load_saved_artifacts()
    root.mainloop()