import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class DateOneLineElement(CompositeElement):
    def __init__(self, parameter, parent, name=None):
        self._month_and_day = None
        self._delimiter = None
        super(DateOneLineElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def draw3(self, drawer, resources, state):

        if self._month_and_day:
            self._month_and_day.draw5(drawer,
                                      resources,
                                      number_array=[state.getTime().month, state.getTime().day],
                                      minimum_digits_array=[2, 2],
                                      force_padding_array=[True, True],
                                      delimiter=self._delimiter)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._month_and_day = NumberElement(parameter, self, 'MonthAndDay')
            return self._month_and_day
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._delimiter = parameter.getValue()
            return ValueElement(parameter, self, 'SeparatorImageIndex')
        else:
            super(DateOneLineElement, self).createChildForParameter(parameter)
