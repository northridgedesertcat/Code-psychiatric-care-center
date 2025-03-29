from pyautogui import moveTo
from random import randint
from pygame import mixer
from os import path
import sys


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


def play_effect_sound(file):
    """ 播放音效（如人物音） """
    # 分配一个空闲通道播放音效
    effect_channel = mixer.find_channel(force=True)  # 强制获取可用通道
    if effect_channel:
        sound = mixer.Sound(file)
        effect_channel.play(sound)


