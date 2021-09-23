from watchFaceParser.elements.gts2mini.activityElements.formattedNumber import FormattedNumber
from watchFaceParser.elements.gts2mini.activityElements.distance import Distance
from watchFaceParser.elements.gts2mini.basicElements.text import Text
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.circleScale import CircleScale
from watchFaceParser.elements.gts2mini.activityElements.caloriesContainer import CaloriesContainer
from watchFaceParser.elements.gts2mini.activityElements.pulseContainer import PulseContainer
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet

class Battery:
    definitions = {
        1: { 'Name': 'BatteryText', 'Type': Text},
        2: { 'Name': 'BatteryIcon', 'Type': ImageSet}
    }
