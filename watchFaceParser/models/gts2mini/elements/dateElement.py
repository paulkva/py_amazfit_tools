import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class DateElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._padding_zero_day = False
        self._monthAndDay = None
        self._monthAndDayAlt = None
        self._padding_zero_month = False
        super(DateElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._monthAndDayAlt:
            self._monthAndDayAlt.draw4(drawer, images, state,
                                    padding_zero_day = self._padding_zero_day,
                                    padding_zero_month= self._padding_zero_month)
        if self._monthAndDay:
            self._monthAndDay.draw4(drawer, images, state,
                                    padding_zero_day = self._padding_zero_day,
                                    padding_zero_month= self._padding_zero_month)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.date.monthAndDayAltElement import MonthAndDayAltElement
            self._monthAndDayAlt = MonthAndDayAltElement(parameter=parameter, parent=self, name='MonthAndDayAlt')
            return self._monthAndDayAlt
        elif parameterId == 2:
            pass
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            self._padding_zero_month = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroMonth')
        elif parameterId == 5:
            self._padding_zero_day = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroDay')
        elif parameterId == 6:
            pass
        elif parameterId == 7:
            pass
        elif parameterId == 8:
            pass
        elif parameterId == 9:
            from watchFaceParser.models.gts2mini.elements.date.monthAndDayElement import MonthAndDayElement
            self._monthAndDay = MonthAndDayElement(parameter=parameter, parent=self, name='MonthAndDay')
            return self._monthAndDay
        else:
            return super(DateElement, self).createChildForParameter(parameter)
