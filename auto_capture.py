import cv2
from datetime import datetime
import os
import time
import pyscreenshot as ImageGrab

def auto_capture():
    while True:
        now_time = datetime.now()
        if now_time.time() < datetime(2018, 11, 8, 7, 0, 0).time():
            continue
        if now_time.time() > datetime(2018, 11, 8, 23, 0, 0).time():
            continue
        imgname_me = now_time.strftime("%Y%m%d_%H%M%S_me.jpg")
        imgname_screen = now_time.strftime("%Y%m%d_%H%M%S_screen.jpg")
        imgdir_me = now_time.strftime("/home/zhaokewei/life/images/日常/%Y%m%d/me")
        imgdir_screen = now_time.strftime("/home/zhaokewei/life/images/日常/%Y%m%d/screen")
        if not os.path.exists(imgdir_me):
            os.makedirs(imgdir_me)
        if not os.path.exists(imgdir_screen):
            os.makedirs(imgdir_screen)
        cap = cv2.VideoCapture(0)
        cap.set(3, 1920)
        cap.set(4, 1080)
        for i in range(10):
            ret, frame = cap.read()
            time.sleep(0.033)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(imgdir_me, imgname_me), frame)
            img_screen = ImageGrab.grab()
            img_screen.save(os.path.join(imgdir_screen, imgname_screen))
        cap.release()
        time.sleep(10 * 60)


if __name__ == '__main__':
    auto_capture()
