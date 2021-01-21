from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 

class Image:
    definitions = {
        1: { 'Name': 'X', 'Type': 'long'},
        2: { 'Name': 'Y', 'Type': 'long'}, 
        4: { 'Name': 'ImageSet', 'Type': [MultilangImage]},
        6: { 'Name': 'ImageUnit', 'Type': [MultilangImage]},
    }