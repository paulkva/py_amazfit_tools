from watchFaceParser.elements.gtr2.screenNormal import ScreenNormal
from watchFaceParser.elements.gtr2.date import Date
from watchFaceParser.elements.gtr2.activity import Activity

class ScreenIdle:
    definitions = { 
        1: { 'Name': 'DialFace', 'Type': ScreenNormal}, 
        2: { 'Name': 'Date', 'Type': Date},
        3: { 'Name': 'Activity', 'Type': [Activity] },   
        4: { 'Name': 'BackgroundImageIndex', 'Type': 'long'}, 
    }
