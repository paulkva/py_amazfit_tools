from watchFaceParser.elements.time import Time
from watchFaceParser.elements.activity import Activity
from watchFaceParser.elements.date import Date
from watchFaceParser.elements.stepsProgress import StepsProgress
from watchFaceParser.elements.status import Status
from watchFaceParser.elements.battery import Battery
from watchFaceParser.elements.analogDialFace2 import AnalogDialFace
from watchFaceParser.elements.unknownType11 import UnknownType11
from watchFaceParser.elements.unknownType14 import UnknownType14
from watchFaceParser.elements.shortcuts import Shortcuts
from watchFaceParser.elements.daysProgress import DaysProgress
from watchFaceParser.elements.weather import Weather

class ScreenNormal:
    definitions = { 
        2: { 'Name': 'AnalogDialFace', 'Type': AnalogDialFace}, 
    }
