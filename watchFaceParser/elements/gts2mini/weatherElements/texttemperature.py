from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutElement import ShortcutElement

class TextTemperature:
    definitions = {
        1: {'Name': 'ImageNumber', 'Type': Number},
        2: {'Name': 'PrefixImageIndex', 'Type': 'long'},
        3: {'Name': 'MinusImageIndex', 'Type': 'long'},
        4: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        5: {'Name': 'NoDataImageIndex', 'Type': 'long'},
        6: {'Name': 'Shortcut', 'Type': ShortcutElement},
    }