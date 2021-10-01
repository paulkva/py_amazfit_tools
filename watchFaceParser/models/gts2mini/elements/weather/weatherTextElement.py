from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class WeatherTextElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._image_number = None
        self._prefix = None
        self._minus = None
        self._suffixC = None
        self._suffixF = None
        self._nodata = None
        super(WeatherTextElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw4(self, drawer, resources, value):

        if self._image_number:
            self._image_number.draw4(drawer,
                                     resources,
                                     value,
                                     minimumDigits = 2,
                                     force_padding = False,
                                     minus = self._minus,
                                     suffix = self._suffixC if self._suffixC else self._suffixF)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'ImageNumber')
            return self._image_number
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._minus = parameter.getValue()
            return ValueElement(parameter, self, 'MinusImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffixC = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndexC')
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffixF = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndexF')
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._nodata = parameter.getValue()
            return ValueElement(parameter, self, 'NoDataImageIndex')
        elif parameterId == 6:  # Shortcut
            pass
        else:
            super(WeatherTextElement, self).createChildForParameter(parameter)
