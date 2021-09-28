from watchFaceParser.elements.gts2mini.basicElements.text import Text
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet
from watchFaceParser.elements.gts2mini.basicElements.scale import Scale

class Battery:
    definitions = {
        1: { 'Name': 'BatteryText', 'Type': Text},
        2: { 'Name': 'ImageProgress', 'Type': ImageSet},
        3: { 'Name': 'IconSetProgress', 'Type': IconSet},
        4: {'Name': 'Unknown4', 'Type': 'long?'},
        5: {'Name': 'Scale', 'Type': Scale},
    }
