from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class Time:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': 'long'},
        2: { 'Name': 'Minutes', 'Type': Number},
        3: { 'Name': 'Seconds', 'Type': Number},
        4: { 'Name': 'Unknown4', 'Type': 'long'},
        5: { 'Name': 'Unknown5', 'Type': 'long'},
        6: {'Name': 'DelimiterMinutes', 'Type': 'long?'},
        7: {'Name': 'DelimiterSeconds', 'Type': 'long?'},
        8: { 'Name': 'MinutesFollowHours', 'Type': 'bool'},
        9: { 'Name': 'SecondsFollowMinutes', 'Type': 'bool'},
        10: { 'Name': 'UnknownCoordinates10', 'Type': Coordinates},
        11: {'Name': 'UnknownCoordinates11', 'Type': Coordinates},
    }

