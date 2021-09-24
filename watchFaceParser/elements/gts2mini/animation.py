from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet

class Progress:
    definitions = {
        1: {'Name': 'Unknown1', 'Type': 'long?'},
        2: { 'Name': 'ImageProgress', 'Type': ImageSet},
        3: { 'Name': 'IconSetProgress', 'Type': IconSet},
        4: {'Name': 'Unknown4', 'Type': 'long?'},
    }

