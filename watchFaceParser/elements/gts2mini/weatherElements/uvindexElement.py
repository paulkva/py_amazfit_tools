from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image


class UVindex:
    definitions = {
        1: {'Name': 'UVindexNumber', 'Type': Number},
        2: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        9: {'Name': 'UVindexIcon', 'Type': Image},
    }

