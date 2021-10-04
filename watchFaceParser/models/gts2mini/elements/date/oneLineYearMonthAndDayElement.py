import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class OneLineYearMonthAndDayElement(CompositeElement):
    def __init__(self, parameter, parent, name=None):
        self._image_number = None
        self._delimiter = None
        super(OneLineYearMonthAndDayElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def draw4(self, drawer, resources, state, padding_zero_day=None, padding_zero_month=None):

        if self._image_number:
            self._image_number.draw5(drawer,
                                     resources,
                                     [ state.getTime().month, state.getTime().day, state.getTime().year],
                                     minimumDigits=2,
                                     force_padding=padding_zero_month,
                                     delimiter=self._delimiter)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'Number')
            return self._image_number
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._delimiter = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterImageIndex')
        else:
            super(OneLineYearMonthAndDayElement, self).createChildForParameter(parameter)
