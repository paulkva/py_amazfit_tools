from watchFaceParser.elements.gts2mini.weatherElements.separate import Separate
from watchFaceParser.elements.gts2mini.weatherElements.unknown2 import Unknown2

class Today:
    definitions = {
        1: { 'Name': 'Separate', 'Type': Separate},
        2: { 'Name': 'OneLine', 'Type': Unknown2},
        3: { 'Name': 'AppendDegreesForBoth', 'Type': 'bool'},
    }
