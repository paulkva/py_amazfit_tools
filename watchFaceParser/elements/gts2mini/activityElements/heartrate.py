from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutElement import ShortcutElement

class HeartRate:
    definitions = {
        1: {'Name': 'ImageNumber', 'Type': Number},
        2: {'Name': 'Unknown2', 'Type': 'long?'},
        3: {'Name': 'NoDataImageIndex', 'Type': 'long'},
        4: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        5: {'Name': 'Icon', 'Type': Image},
        6: {'Name': 'Shortcut', 'Type': ShortcutElement},
    }