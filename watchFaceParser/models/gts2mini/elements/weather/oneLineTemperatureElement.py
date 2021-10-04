import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class OneLineTemperatureElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._oneLineMinMax = None
        super(OneLineTemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        if self._oneLineMinMax:
            self._oneLineMinMax.draw4(drawer, resources, state.getCurrentTemperature()-10, state.getCurrentTemperature()+10)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.weather.oneLineTemperatureMinMaxElement import OneLineMinMaxTemperatureElement
            self._oneLineMinMax = OneLineMinMaxTemperatureElement(parameter = parameter, parent = self, name = 'OneLineMinMax')
            return self._oneLineMinMax
        else:
            print ("Unknown OneLineTemperatureElement",parameterId)
            return super(OneLineTemperatureElement, self).createChildForParameter(parameter)
