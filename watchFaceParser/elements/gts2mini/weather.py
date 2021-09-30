from watchFaceParser.elements.gts2mini.weatherElements.temperature import Temperature
from watchFaceParser.elements.gts2mini.weatherElements.humidity import Humidity
from watchFaceParser.elements.gts2mini.weatherElements.uvindexElement import UVindex
from watchFaceParser.elements.gts2mini.weatherElements.icon import Icon


class Weather:
    definitions = {
        1: {'Name': 'Icon', 'Type': Icon},
        2: {'Name': 'Temperature', 'Type': Temperature},
        3: {'Name': 'Unknown3', 'Type': 'long?'},
        4: {'Name': 'Humidity', 'Type': Humidity},
        6: {'Name': 'UVindex', 'Type': UVindex},
    }

