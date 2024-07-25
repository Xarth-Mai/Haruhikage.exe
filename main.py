import pygame
import time
import sys
import os

# 初始化 pygame 音频模块
pygame.mixer.init()

# 确定音频文件的路径
if getattr(sys, 'frozen', False):
    # 运行在打包的应用程序中
    audio_file_path = os.path.join(sys._MEIPASS, 'haruhikage_mygo.wav')
else:
    # 运行在开发环境中
    audio_file_path = 'haruhikage_mygo.wav'

# 加载音频文件
pygame.mixer.music.load(audio_file_path)

# 播放音频
pygame.mixer.music.play()

# 等待音频播放完成
while pygame.mixer.music.get_busy():
    time.sleep(1)
