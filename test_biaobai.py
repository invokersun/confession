import tkinter as tk
from tkinter import messagebox
import random


class ConfessionApp:
    def __init__(self, master):
        self.master = master
        master.title("重要问题")
        master.geometry("400x300")

        # 阻止直接关闭窗口
        master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # 创建界面元素
        self.create_widgets()

        # 不同意按钮的移动参数
        self.disagree_positions = [
            (280, 200), (150, 100), (50, 250),
            (200, 50), (300, 150), (100, 180)
        ]
        self.disagree_texts = [
            "再考虑一下", "真的不要吗", "你忍心拒绝吗",
            "给个机会嘛", "我可喜欢你了", "要不要再想想"
        ]
        self.disagree_index = 0

    def create_widgets(self):
        # 问题标签
        self.label = tk.Label(
            self.master,
            text="xxx同志，你愿意做我的女朋友吗？",
            font=("微软雅黑", 16)
        )
        self.label.pack(pady=50)

        # 同意按钮
        self.agree_btn = tk.Button(
            self.master,
            text="愿意",
            command=self.agree,
            font=("微软雅黑", 12),
            bg="pink",
            width=10
        )
        self.agree_btn.pack(side=tk.LEFT, padx=50)

        # 不同意按钮
        self.disagree_btn = tk.Button(
            self.master,
            text="不愿意",
            command=self.move_disagree,
            font=("微软雅黑", 12),
            bg="lightblue",
            width=10
        )
        self.disagree_btn.place(x=280, y=200)

    def agree(self):
        # 创建新窗口
        new_window = tk.Toplevel(self.master)
        new_window.title("❤")
        new_window.geometry("300x150")

        tk.Label(
            new_window,
            text="我也愿意！❤",
            font=("微软雅黑", 20),
            fg="red"
        ).pack(expand=True)

        # 5秒后关闭程序
        self.master.after(3000, self.master.destroy)

    def move_disagree(self):
        # 随机移动按钮位置并改变文字
        x, y = random.choice(self.disagree_positions)
        self.disagree_btn.place(x=x, y=y)

        # 循环显示不同文字
        self.disagree_btn.config(
            text=self.disagree_texts[self.disagree_index % len(self.disagree_texts)]
        )
        self.disagree_index += 1

    def on_closing(self):
        # 关闭窗口时的处理
        messagebox.showinfo(
            "不许关！",
            "不回答就想关闭，没门！"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = ConfessionApp(root)
    root.mainloop()