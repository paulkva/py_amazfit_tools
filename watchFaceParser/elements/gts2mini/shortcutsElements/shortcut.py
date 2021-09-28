from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element
from watchFaceParser.models.gts2mini.shortcutType import ShortcutType

class Shortcut:
    definitions = {
        1: { 'Name': 'Icon', 'Type': Image},
        2: { 'Name': 'ShortcutType', 'Type': ShortcutType}, # 5 - Calories, 16 - Music
        3: { 'Name': 'Element', 'Type': Element},
    }
