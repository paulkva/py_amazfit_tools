from watchFaceParser.elements.analogDialFaceElements.clockHand2 import ClockHand
from watchFaceParser.elements.basicElements.image import Image

class AnalogDialFace:
    definitions = {
        1: { 'Name': 'Hours', 'Type': ClockHand},
        2: { 'Name': 'Minutes', 'Type': ClockHand},
        3: { 'Name': 'Seconds', 'Type': ClockHand},
        4: { 'Name': 'SecCenterImage', 'Type': Image}, # verge
        5: { 'Name': 'HourCenterImage', 'Type': Image}, # testit!
        6: { 'Name': 'MinCenterImage', 'Type': Image}, # testit!
    }

