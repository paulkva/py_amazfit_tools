from watchFaceParser.elements.gtr2.status import Status
from watchFaceParser.elements.gtr2.activity import Activity
from watchFaceParser.elements.gtr2.date import Date 

class System:
    definitions = {
        1: { 'Name': 'Status', 'Type': Status },   
        2: { 'Name': 'Date', 'Type': Date },   
        3: { 'Name': 'Activity', 'Type': [Activity] },   
    }