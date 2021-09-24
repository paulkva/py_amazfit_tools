from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet
from watchFaceParser.elements.gts2mini.basicElements.scale import Scale

class Progress:
    definitions = {
        1: {'Name': 'Unknown1', 'Type': 'long?'},
        2: { 'Name': 'ImageProgress', 'Type': ImageSet},
        3: { 'Name': 'IconSetProgress', 'Type': IconSet},
        4: {'Name': 'Unknown4', 'Type': 'long?'},
        5: {'Name': 'Unknown5', 'Type': 'long?'},
        6: {'Name': 'Scale', 'Type': Scale},
    }

