from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet

class ImageSetAnimation:
    definitions = {
        1: {'Name': 'ImageProgress', 'Type': ImageSet},
        2: {'Name': 'FrameInterval', 'Type': 'long'}, #msec
        3: {'Name': 'PlayTimes', 'Type': 'long'}, #255 if unlimited loops
        4: {'Name': 'Repeat', 'Type': 'bool'},
    }