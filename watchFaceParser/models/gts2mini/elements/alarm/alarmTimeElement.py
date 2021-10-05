import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class AlarmTimeElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._delimiter = False
        self._padding_zero_hours = False
        self._padding_zero_minutes = None
        super(AlarmTimeElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        followxy = None
        if self._hours:
            followxy = self._hours.draw4(drawer, images, state.getTime().hour, 2,
                                         force_padding = self._padding_zero_hours,
                                         followxy = None,
                                         suffix = self._delimiter)

        if self._minutes:
            followxy = self._minutes.draw4(drawer, images, state.getTime().month, 2,
                                           force_padding = self._padding_zero_minutes,
                                           followxy = None,
                                           suffix = None)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._hours = NumberElement(parameter=parameter, parent=self, name='Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._minutes = NumberElement(parameter=parameter, parent=self, name='Minutes')
            return self._minutes
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            pass
        elif parameterId == 5:
            self._delimiter = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterMinutes')
        elif parameterId == 6:
            pass
        elif parameterId == 7:
            self._padding_zero_hours = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroHours')
        elif parameterId == 8:
            self._padding_zero_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroMinutes')
        elif parameterId == 9:
            pass
        elif parameterId == 10:
            pass
        elif parameterId == 11:
            pass
        else:
            return super(AlarmTimeElement, self).createChildForParameter(parameter)

