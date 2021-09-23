from watchFaceParser.elements.gts2mini.basicElements.circleScale import CircleScale
from watchFaceParser.elements.gts2mini.analogDialFaceElements.clockHand import ClockHand 

class CaloriesContainer:
    definitions = {
        1: { 'Name': 'Circle', 'Type': CircleScale}, # should be kcal on gts
        3: { 'Name': 'ClockHand', 'Type': ClockHand}, # gtr - Red flywheel
    }
