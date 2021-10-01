from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutElement import ShortcutElement

class UVindex:
    definitions = {
        1: {'Name': 'UVindexNumber', 'Type': Number},
        2: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        3: {'Name': 'Shortcut', 'Type': ShortcutElement},
        9: {'Name': 'UVindexIcon', 'Type': Image},
    }

