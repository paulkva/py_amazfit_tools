from watchFaceParser.elements.gtr2.status import Status
from watchFaceParser.elements.gtr2.heartRate import HeartRate
from watchFaceParser.elements.gtr2.date import Date

class System:
    definitions = {
        1: { 'Name': 'Status', 'Type': Status },   
        2: { 'Name': 'Date', 'Type': Date },   
        3: { 'Name': 'HearRate', 'Type': HeartRate },   
    }