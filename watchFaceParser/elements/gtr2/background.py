from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 

class Background:
    definitions = {
        1: { 'Name': 'Preview', 'Type': [MultilangImage]}, #add array support for different laguages
        2: { 'Name': 'BackgroundImageIndex', 'Type': 'long'}, 
    }