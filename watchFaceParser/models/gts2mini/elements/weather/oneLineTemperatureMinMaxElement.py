import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement


class OneLineMinMaxTemperatureElement(CompositeElement):
    def __init__(self, parameter, parent, name=None):
        self._image_number = None
        self._prefix = None
        self._minus = None
        self._delimiter = None
        self._degrees = None
        super(OneLineMinMaxTemperatureElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def draw4(self, drawer, resources, min, max):

        if self._image_number:
            self._image_number.draw5(drawer,
                                     resources,
                                     number_array=[min, max],
                                     minimum_digits_array=[2, 2],
                                     force_padding_array=[False, False],
                                     minus=self._minus,
                                     delimiter=self._delimiter,
                                     suffix=self._degrees)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'Number')
            return self._image_number
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._minus = parameter.getValue()
            return ValueElement(parameter, self, 'MinusImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._delimiter = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterImageIndex')
        elif parameterId == 4: # UnknownLong4
            pass
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._degrees = parameter.getValue()
            return ValueElement(parameter, self, 'DegreesImageIndex')
        elif parameterId == 6:
            pass
        else:
            super(OneLineMinMaxTemperatureElement, self).createChildForParameter(parameter)
