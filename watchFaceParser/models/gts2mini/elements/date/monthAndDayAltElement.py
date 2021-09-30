import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class MonthAndDayAltElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):

        self._month = None
        self._day = None

        super(MonthAndDayAltElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw4(self, drawer, images, state, padding_zero_day = False, padding_zero_month = False, padding_zero_year = False):
        followxy = None

        if self._month:
            followxy = self._month.draw4(drawer, images, state.getTime().month, 2,
                            force_padding = padding_zero_month,
                            followxy = followxy,
                            decimal_pointer = None,
                            minus = None,
                            prefix = None,
                            suffix = None)

        if self._day:
            followxy = self._day.draw4(drawer, images, state.getTime().day, 2,
                            force_padding = padding_zero_day,
                            followxy = None,
                            decimal_pointer = None,
                            minus = None,
                            prefix = None,
                            suffix = None)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._month = NumberElement(parameter=parameter, parent=self, name='Month')
            return self._month
        elif parameterId == 2:
            pass
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._day = NumberElement(parameter=parameter, parent=self, name='Day')
            return self._day
        else:
            return super(MonthAndDayAltElement, self).createChildForParameter(parameter)

