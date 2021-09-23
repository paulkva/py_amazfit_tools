from watchFaceParser.elements.gts2mini.activityElements.steps import Steps
from watchFaceParser.elements.gts2mini.activityElements.calories import Calories
from watchFaceParser.elements.gts2mini.activityElements.heartrate import HeartRate
from watchFaceParser.elements.gts2mini.activityElements.distance import Distance
from watchFaceParser.elements.gts2mini.activityElements.pai import PAI

class Activity:
    definitions = {
        1: { 'Name': 'Steps', 'Type': Steps},
        3: { 'Name': 'Calories', 'Type': Calories},
        4: { 'Name': 'HeartRate', 'Type': HeartRate},
        5: { 'Name': 'Distance', 'Type': Distance},
        6: { 'Name': 'PAI', 'Type': PAI},
        7: { 'Name': 'Unknown7', 'Type': 'long'},
    }
