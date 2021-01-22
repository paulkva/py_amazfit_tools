from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 
from watchFaceParser.models.color import Color

class Background:
    definitions = {
        1: { 'Name': 'Preview', 'Type': [MultilangImage]},
        2: { 'Name': 'BackgroundImageIndex', 'Type': 'long'}, 
        3: { 'Name': 'Color', 'Type': Color}, 
    }