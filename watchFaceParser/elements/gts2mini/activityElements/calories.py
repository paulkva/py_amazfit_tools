from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element

class Calories:
    definitions = {
        1: {'Name': 'ImageNumber', 'Type': Number},
        2: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        3: {'Name': 'Icon', 'Type': Image},
        4: {'Name': 'Shortcut', 'Type': Element},
    }