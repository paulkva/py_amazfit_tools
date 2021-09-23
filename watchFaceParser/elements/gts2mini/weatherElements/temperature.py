from watchFaceParser.elements.gts2mini.basicElements.text import Text
from watchFaceParser.elements.gts2mini.weatherElements.today import Today
from watchFaceParser.elements.gts2mini.weatherElements.symbols import Symbols
from watchFaceParser.elements.gts2mini.basicElements.circleScale import CircleScale

class Temperature:
    definitions = {
        1: { 'Name': 'Current', 'Type': Text},
        2: { 'Name': 'Today', 'Type': Today},
        3: { 'Name': 'Symbols', 'Type': Symbols},
        4: { 'Name': 'TemperatureMeter', 'Type': CircleScale}, #gts- Fluorescence
    }

