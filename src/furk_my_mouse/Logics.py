from pyautogui import moveTo
from random import randint
from pygame import mixer
from os import path
import sys
import tkinter as tk
from PIL import Image, ImageTk


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)


def move_mouse(screen_width, screen_height):
    while True:
        moveTo(randint(1,screen_width),randint(1,screen_height), duration=0.01)

def playsounds(File):
    mixer.init()
    mixer.music.load(File)
    mixer.music.play(-1)

def showPhotos(ph,max_occupancy=0.8):
    root = tk.Tk()
    root.overrideredirect(True)

    img = Image.open(ph)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算最大允许尺寸
    max_width = int(screen_width * max_occupancy)
    max_height = int(screen_height * max_occupancy)

    # 按比例缩放
    width_ratio = max_width / img.width
    height_ratio = max_height / img.height
    scale = min(width_ratio, height_ratio)

    new_size = (
        int(img.width * scale),
        int(img.height * scale)
    )
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 计算居中坐标
    x = (screen_width - img.width) // 2
    y = (screen_height - img.height) // 2
    # 设置窗口位置和尺寸（居中显示）
    root.geometry(f"{img.width}x{img.height}+{x}+{y}")
    # 显示图片
    label = tk.Label(root, image=photo)
    label.pack()

    # 初始透明度
    current_alpha = 1.0
    root.attributes('-alpha', current_alpha)
    blink_speed = 100
    # 闪烁动画
    def blink():
        nonlocal current_alpha
        # 在 0.3~1.0 之间循环变化透明度
        current_alpha = 0.01 if current_alpha > 0.5 else 1.0
        root.attributes('-alpha', current_alpha)
        root.after(blink_speed, blink)  # 持续闪烁

    # 启动闪烁
    blink()
    # 自动关闭
    root.after(800, root.destroy)
    # 保持图片引用
    root.mainloop()


