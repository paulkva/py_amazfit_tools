from watchFaceParser.elements.gts2mini.analogDialFaceElements.clockHand import ClockHand
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class AnalogDialFace:
    definitions = {
        1: {'Name': 'Unknown1', 'Type': 'long?'},
        2: {'Name': 'CommonCenterCoordinates', 'Type': Coordinates}, #c695a02e7f899736773c32dcfb929a54.bin, one center for all clock hands
        3: {'Name': 'Hours', 'Type': ClockHand},
        4: {'Name': 'Minutes', 'Type': ClockHand},
        5: {'Name': 'Seconds', 'Type': ClockHand},
    }
