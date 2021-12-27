from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element


class TextTemperature:
    definitions = {
        1: {'Name': 'ImageNumber', 'Type': Number},
        2: {'Name': 'MinusImageIndex', 'Type': 'long'},
        3: {'Name': 'SuffixImageIndexC', 'Type': 'long'},
        4: {'Name': 'SuffixImageIndexF', 'Type': 'long'},
        5: {'Name': 'NoDataImageIndex', 'Type': 'long'},
        6: {'Name': 'Shortcut', 'Type': Element},
    }