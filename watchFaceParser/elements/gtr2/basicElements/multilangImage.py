#from watchFaceParser.models.textAlignment import TextAlignment
from watchFaceParser.elements.gtr2.basicElements.imageSet import ImageSetGTR2
from watchFaceParser.models.gtr2.langCodeType import LangCodeType

class MultilangImage:
    definitions = { 
        1: { 'Name': 'LangCode', 'Type': LangCodeType}, 
        2: { 'Name': 'ImageSet', 'Type': ImageSetGTR2},
    }