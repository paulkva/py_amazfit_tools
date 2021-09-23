from watchFaceParser.elements.gts2mini.analogDialFaceElements.clockHand import ClockHand
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class AnalogDialFaceAOD:
    definitions = {
        1: { 'Name': 'CenterCoordinates', 'Type': Coordinates},
        2: { 'Name': 'Hours', 'Type': ClockHand},
        3: { 'Name': 'Minutes', 'Type': ClockHand},
    }

