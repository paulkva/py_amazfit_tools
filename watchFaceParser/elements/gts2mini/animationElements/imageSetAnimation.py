from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet

class ImageSetAnimation:
    definitions = {
        1: { 'Name': 'ImageProgress', 'Type': ImageSet},
        2: { 'Name': 'Unknown2', 'Type': 'long'},
        3: {'Name': 'Unknown3', 'Type': 'long'},
        4: {'Name': 'Repeat', 'Type': 'bool'},
    }