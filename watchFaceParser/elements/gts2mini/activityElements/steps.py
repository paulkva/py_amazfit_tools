from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutElement import ShortcutElement

class Steps:
    definitions = {
        1: {'Name': 'ImageNumber', 'Type': Number},
        2: {'Name': 'PrefixImageIndex', 'Type': 'long'},
        3: {'Name': 'NoDataImageIndex', 'Type': 'long'},
        4: {'Name': 'Icon', 'Type': Image},
        6: {'Name': 'Shortcut', 'Type': ShortcutElement},
        7: {'Name': 'SuffixImageIndex', 'Type': 'long'},
    }