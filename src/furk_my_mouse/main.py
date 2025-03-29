import pyautogui
import Logics
from time import sleep
from threading import Thread



#configs

#获取屏幕大小
screen_width, screen_height = pyautogui.size()

#操作间隔
pyautogui.PAUSE=0.01

#禁用故障保护
#注意！！！！！！！！！禁用将会强行夺取光标无法中断，除非你结束指定进程
#如果你是个大黑客，会进程隐藏技术几乎可以永飞雷神
pyautogui.FAILSAFE=True

#延时启动
sleepTime=0

#是否播放声音
playsounds=True
#播放的音乐数量，比如可以分为背景音与人声，也可以之播放一个
morePlay=False
#音乐类型仅支持wav
soundBackground=Logics.resource_path("wavs/batty.mp3")
soundGhost=Logics.resource_path("wavs/lau.wav")



if __name__=="__main__":
    sleep(sleepTime)
    if playsounds:
        t=Thread(target=Logics.playsounds, args=(soundBackground,))
        t.start()
        if morePlay:
            t2 = Thread(target=Logics.play_effect_sound, args=(soundGhost,))
            t2.start()
    Logics.move_mouse(screen_width, screen_height)