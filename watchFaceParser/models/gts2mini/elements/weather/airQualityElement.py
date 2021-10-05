import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class AirQualityElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._suffix = None
        self._image = None
        super(AirQualityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        if self._number:
            self._number.draw4(drawer, resources, state.getAirQuality(), suffix = self._suffix)

        if self._image:
            self._image.draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter, self, 'AirQualityNumber')
            return self._number
        if parameterId == 2:
            pass
        if parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._image = ImageElement(parameter, self, 'AirQualityIcon')
            return self._image
        else:
            print ("Unknown AirQualityElement",parameterId)
            super(AirQualityElement, self).createChildForParameter(parameter)
