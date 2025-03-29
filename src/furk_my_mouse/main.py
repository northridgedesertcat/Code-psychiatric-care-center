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

#音乐类型仅支持wav
soundBackground=Logics.resource_path("wavs/lau.wav")


#开始之前弹一张图片
photoPath=Logics.resource_path("wavs/22.webp")
showPhoto=True
#图片占屏幕的大小比例
max_occupancy=0.8


if __name__=="__main__":
    sleep(sleepTime)
    if showPhoto:
        Logics.showPhotos(photoPath,max_occupancy)
    if playsounds:
        t=Thread(target=Logics.playsounds, args=(soundBackground,))
        t.start()
    Logics.move_mouse(screen_width, screen_height)