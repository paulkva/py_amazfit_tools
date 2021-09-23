from watchFaceParser.elements.gts2mini.weatherElements.temperature import Temperature
from watchFaceParser.elements.gts2mini.weatherElements.icon import Icon


class Weather:
    definitions = {
        1: { 'Name': 'Icon', 'Type': Icon},
        2: { 'Name': 'Temperature', 'Type': Temperature},
    }

