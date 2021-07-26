import os
import cv2
from base_camera import BaseCamera
import time
import numpy as np
import cv2
import time
import multiprocessing as mp
import time
from datetime import datetime
import numpy as np  # 实际使用的时候记得放在外面
from packCode.dataProcess import paroImgOutput
from multiprocessing.shared_memory import SharedMemory


class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()
        # self.existing_shm = self.shared_memory.SharedMemory(name='unclezhanimg12345')

    def __del__(self):
        print('这是析构函数')
        self.existing_shm.close()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        print('进入opencv')
        # imgInfo = cap1.shape
        # size = (imgInfo[1], imgInfo[0])  # 获取图片宽高度信息
        # print(size)
        while True:
            # img = cv2.imread('/root/flask-video-streaming-master/packCode/tmp.jpg')
            existing_shm = SharedMemory(name='unclezhanimg12345')
            print('existing_shm', existing_shm)

            image = np.ndarray((960, 1260, 3), dtype='uint8', buffer=existing_shm)
            print('image.shape:  ', image.shape)

            time.sleep(0.01)
            yield image


if __name__ == '__main__':
    # parameters = np.load('D:/Desktop/ctmx/Tugmaster0617/Tugmaster/Backend/packCode/parameters.npy')
    camera1 = Camera()
    camera1.frames()