from watchFaceParser.elements.gts2mini.deviceId import DeviceId
from watchFaceParser.elements.gts2mini.background import Background
from watchFaceParser.elements.gts2mini.timeDigital import TimeDigital
from watchFaceParser.elements.gts2mini.activity import Activity
from watchFaceParser.elements.gts2mini.dateblock import DateBlock
from watchFaceParser.elements.gts2mini.battery import Battery
from watchFaceParser.elements.gts2mini.analogDialFace import AnalogDialFace
from watchFaceParser.elements.gts2mini.progress import Progress
from watchFaceParser.elements.gts2mini.status import Status
from watchFaceParser.elements.gts2mini.weather import Weather

class WatchFace:
    definitions = {
        0: { 'Name': 'Info', 'Type': DeviceId},
        2: { 'Name': 'Background', 'Type': Background},
        4: { 'Name': 'Activity', 'Type': Activity},
        5: { 'Name': 'DateBlock', 'Type': DateBlock},
        6: { 'Name': 'Weather', 'Type': Weather},
        7: {'Name': 'StepProgress', 'Type': Progress},
        8: {'Name': 'Status', 'Type': Status},
        9: { 'Name': 'Battery', 'Type': Battery},
        11: { 'Name': 'Unknown11', 'Type': 'long?'}, # Animation ?
        12: {'Name': 'HearthProgress', 'Type': Progress},
        20: {'Name': 'TimeAnalog', 'Type': AnalogDialFace},
        21: {'Name': 'TimeDigital', 'Type': TimeDigital},
        29: {'Name': 'Unknown29', 'Type': 'long?'}, # is this aod screen?
    }
