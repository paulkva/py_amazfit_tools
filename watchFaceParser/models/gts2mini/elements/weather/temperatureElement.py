import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class TemperatureElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._current = None
        super(TemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        if self._current:
            self._current.draw4(drawer, resources, state.getCurrentTemperature())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.weather.weatherTextElement import WeatherTextElement
            self._current = WeatherTextElement(parameter, self, 'Current')
            return self._current
        else:
            print ("Unknown TemperatureElement",parameterId)
            super(TemperatureElement, self).createChildForParameter(parameter)
