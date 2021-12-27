from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutElement import ShortcutElement

class Calories:
    definitions = {
        1: {'Name': 'ImageNumber', 'Type': Number},
        2: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        3: {'Name': 'Icon', 'Type': Image},
        4: {'Name': 'Shortcut', 'Type': ShortcutElement},
    }