# cam.py

import camera
import cam_config as cc

class EspCam:
    def __init__(self):
        cc.configure(camera, cc.ai_thinker)
#         camera.conf(cc.FRAMESIZE, cc.FRAMESIZE_QVGA)#->320x240->np.zeros((240, 320, 3), np.uint8)
        camera.conf(cc.FRAMESIZE, cc.FRAMESIZE_HVGA)#->480x320->np.zeros((320, 480, 3), np.uint8)
        self.INIT = camera.init() 
        if self.INIT == True:
            print("Camera init success")
        else:
            print("Camera init error")
    
    def capture(self):
        if self.INIT != True:
            print("Unable to capture: Camera init error.")
            return
        img = camera.capture()
        if (len(img) > 0):
            return img
        else:
            print("Error")
            self.capture()

    def __del__(self):
        print("Camera deinit...")
        camera.deinit()
