import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class DateElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._padding_zero_day = False
        self._yearMonthAndDay = None
        self._monthAndDayAlt = None
        self._oneLineMonthAndDay = None
        self._oneLineYearMonthAndDay = None
        self._padding_zero_month = False
        super(DateElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._monthAndDayAlt:
            self._monthAndDayAlt.draw4(drawer, images, state,
                                       padding_zero_day = self._padding_zero_day,
                                       padding_zero_month= self._padding_zero_month)

        if self._oneLineMonthAndDay:
            self._oneLineMonthAndDay.draw4(drawer, images, state,
                                           padding_zero_day = self._padding_zero_day,
                                           padding_zero_month=self._padding_zero_month)

        if self._oneLineYearMonthAndDay:
            self._oneLineYearMonthAndDay.draw4(drawer, images, state,
                                               padding_zero_day = self._padding_zero_day,
                                               padding_zero_month=self._padding_zero_month)

        if self._yearMonthAndDay:
            self._yearMonthAndDay.draw4(drawer, images, state,
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
            from watchFaceParser.models.gts2mini.elements.date.oneLineMonthAndDayElement import OneLineMonthAndDayElement
            self._oneLineMonthAndDay = OneLineMonthAndDayElement(parameter=parameter, parent=self, name='OneLineMonthAndDay')
            return self._oneLineMonthAndDay
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.date.oneLineYearMonthAndDayElement import OneLineYearMonthAndDayElement
            self._oneLineYearMonthAndDay = OneLineYearMonthAndDayElement(parameter=parameter, parent=self, name='OneLineYearMonthAndDay')
            return self._oneLineYearMonthAndDay
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
            from watchFaceParser.models.gts2mini.elements.date.yearMonthAndDayElement import YearMonthAndDayElement
            self._yearMonthAndDay = YearMonthAndDayElement(parameter=parameter, parent=self, name='YearMonthAndDay')
            return self._yearMonthAndDay
        else:
            return super(DateElement, self).createChildForParameter(parameter)
