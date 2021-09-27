import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class MonthAndDayElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._year = None
        self._month = None
        self._day = None
        self._delimiter_month = None
        self._delimiter_day = None
        self._delimiter_year = None
        self._month_as_word = None
        super(MonthAndDayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)
    #
    #     if self.getDigit().getPaddingZero():
    #         return self.getDigit().draw4(drawer, resources, state.getTime().year % 2000, 2, 2)
    #     else:
    #         return self.getDigit().draw4(drawer, resources, state.getTime().year, 4, 4)
    #
    # if self._dateType == 1:
    #     return self.getDigit().draw4(drawer, resources, state.getTime().month, 2, 2, followxy)
    # if self._dateType == 2:
    #     return self.getDigit().draw4(drawer, resources, state.getTime().day, 2, 2, followxy)

    def draw4(self, drawer, images, state, padding_zero_day = False, padding_zero_month = False, padding_zero_year = False):
        if self._day:
            self._day.draw4(drawer, images, state.getTime().day, 2,
                            force_padding = padding_zero_day,
                            followxy = None,
                            decimal_pointer = None,
                            minus = None,
                            prefix = None,
                            suffix = self._delimiter_day)
        if self._month:
            self._month.draw4(drawer, images, state.getTime().month, 2,
                            force_padding = padding_zero_month,
                            followxy = None,
                            decimal_pointer = None,
                            minus = None,
                            prefix = None,
                            suffix = self._delimiter_month)
        if self._month_as_word:
            self._month_as_word.draw3(drawer, images, state.getTime().month)
            
        if self._year:
            self._year.draw4(drawer, images, state.getTime().year, 4,
                            force_padding = padding_zero_year,
                            followxy = None,
                            decimal_pointer = None,
                            minus = None,
                            prefix = None,
                            suffix = self._delimiter_year)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._year = NumberElement(parameter=parameter, parent=self, name='Year')
            return self._year
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._month = NumberElement(parameter=parameter, parent=self, name='Month')
            return self._month
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._day = NumberElement(parameter=parameter, parent=self, name='Day')
            return self._day
        elif parameterId == 4:
            pass
        elif parameterId == 5:
            pass
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._month_as_word = ImageSetElement(parameter=parameter, parent=self, name='MonthAsWord')
            return self._month_as_word
        elif parameterId == 7:
            pass
        elif parameterId == 8:
            pass
        elif parameterId == 9:
            pass
        elif parameterId == 10:
            pass
        elif parameterId == 11:
            pass
        elif parameterId == 12:
            self._delimiter_month = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterMonthImageIndex')
        elif parameterId == 13:
            pass
        else:
            return super(MonthAndDayElement, self).createChildForParameter(parameter)

