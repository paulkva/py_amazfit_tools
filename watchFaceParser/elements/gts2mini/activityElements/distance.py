from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutElement import ShortcutElement
from watchFaceParser.elements.basicElements.coordinates import Coordinates
class Distance:
    definitions = {
        1: { 'Name': 'ImageNumber', 'Type': Number},
        2: { 'Name': 'SuffixImageIndexKM', 'Type': 'long'},
        3: { 'Name': 'DecimalPointImageIndex', 'Type': 'long'},
        4: {'Name': 'SuffixImageIndexMI', 'Type': 'long'},
        5: {'Name': 'Icon', 'Type': Image},
        6: {'Name': 'Shortcut', 'Type': ShortcutElement},
        8: {'Name': 'SuffixImageCoordinates', 'Type': Coordinates},
    }

