from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image

class AirQuality:
    definitions = {
        1: {'Name': 'AirQualityNumber', 'Type': Number},
        3: {'Name': 'AirQualityIcon', 'Type': Image},
    }

