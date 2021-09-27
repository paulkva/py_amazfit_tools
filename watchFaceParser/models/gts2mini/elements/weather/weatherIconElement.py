import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement


class WeatherIconElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._images = None
        super(WeatherIconElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        if self._images:
            self._images.draw3(drawer, resources, state.getCurrentWeather())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._images = ImageSetElement(parameter, self, 'Images')
            return self._images
        else:
            super(WeatherIconElement, self).createChildForParameter(parameter)
