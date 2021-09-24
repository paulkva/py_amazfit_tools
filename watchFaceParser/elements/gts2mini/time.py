from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class Time:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': 'long'},
        2: { 'Name': 'Minutes', 'Type': Number},
        3: { 'Name': 'Seconds', 'Type': Number},
        4: { 'Name': 'Unknown4', 'Type': 'long'},
        5: { 'Name': 'Unknown5', 'Type': 'long'},
        6: {'Name': 'Unknown6', 'Type': 'long?'},
        7: {'Name': 'Unknown7', 'Type': 'long?'},
        8: { 'Name': 'Unknown8', 'Type': 'long'},
        9: { 'Name': 'Unknown9', 'Type': 'long'},
        10: { 'Name': 'Unknown10', 'Type': 'long'},
        11: {'Name': 'UnknownCoordinates11', 'Type': Coordinates},
    }

