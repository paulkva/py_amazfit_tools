import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class WeekDayElement(CompositeElement):
    def __init__(self, parameter, parent, name=None):
        self._weekdayImage = None
        super(WeekDayElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def draw3(self, drawer, resources, state):

        if self._weekdayImage:
            self._weekdayImage.draw3(drawer, resources, state.getTime().weekday())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._weekdayImage = ImageSetElement(parameter, self, 'Weekday')
            return self._weekdayImage
        elif parameterId == 2:
            pass
        elif parameterId == 3:
            pass
        else:
            super(WeekDayElement, self).createChildForParameter(parameter)
