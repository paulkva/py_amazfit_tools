from watchFaceParser.elements.gts2mini.weatherElements.texttemperature import TextTemperature
from watchFaceParser.elements.gts2mini.weatherElements.today import Today
from watchFaceParser.elements.gts2mini.weatherElements.symbols import Symbols
from watchFaceParser.elements.gts2mini.basicElements.circleScale import CircleScale

class Temperature:
    definitions = {
        1: {'Name': 'Current', 'Type': TextTemperature},
        3: {'Name': 'Lowest', 'Type': TextTemperature},
        4: {'Name': 'Highest', 'Type': TextTemperature},
    }

