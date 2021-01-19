from watchFaceParser.elements.deviceId import DeviceId
from watchFaceParser.elements.background2 import Background
from watchFaceParser.screenNormal import ScreenNormal
from watchFaceParser.screenIdle import ScreenIdle

class WatchFace:
    definitions = {
        0: { 'Name': 'Info', 'Type': DeviceId},
        3: { 'Name': 'Background', 'Type': Background},
        4: { 'Name': 'ScreenNormal', 'Type': ScreenNormal},
        10: { 'Name': 'ScreenIdle', 'Type': ScreenIdle},
    }
