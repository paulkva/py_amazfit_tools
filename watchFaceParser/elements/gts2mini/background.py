from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.models.color import Color

class Background:
    definitions = {
        1: { 'Name': 'Image', 'Type': Image},
        2: { 'Name': 'BackgroundColor', 'Type': Color},
        3: { 'Name': 'Preview', 'Type': Image},
        4: { 'Name': 'PreviewKorean', 'Type': Image},
        5: { 'Name': 'PreviewChinese', 'Type': Image},
        6: { 'Name': 'FloatingLayer', 'Type': Image},
    }