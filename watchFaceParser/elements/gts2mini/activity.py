from watchFaceParser.elements.gts2mini.activityElements.steps import Steps
from watchFaceParser.elements.gts2mini.activityElements.calories import Calories
from watchFaceParser.elements.gts2mini.activityElements.heartrate import HeartRate
from watchFaceParser.elements.gts2mini.activityElements.distance import Distance
from watchFaceParser.elements.gts2mini.activityElements.pai import PAI
from watchFaceParser.elements.gts2mini.activityElements.standup import StandUp
from watchFaceParser.elements.gts2mini.basicElements.image import Image

class Activity:
    definitions = {
        1: { 'Name': 'Steps', 'Type': Steps},
        2: { 'Name': 'Icon', 'Type': Image},
        3: { 'Name': 'Calories', 'Type': Calories},
        4: { 'Name': 'HeartRate', 'Type': HeartRate},
        5: { 'Name': 'Distance', 'Type': Distance},
        6: { 'Name': 'PAI', 'Type': PAI},
        7: { 'Name': 'UnknownLongValue7', 'Type': 'long'}, # always 0
        8: { 'Name': 'StandUp', 'Type': StandUp},
    }
