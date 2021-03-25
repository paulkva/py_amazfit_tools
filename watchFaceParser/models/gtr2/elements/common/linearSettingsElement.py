import logging
from watchFaceParser.config import Config

from watchFaceParser.models.gtr2.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.gtr2.elements.common.multilangImageElement import MultilangImageElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper

class LinearSettingsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._startX = None
        self._startY = None
        self._endX = None
        self._endY = None
        super(LinearSettingsElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def getStartX(self):
        return self._startX

    def getStartY(self):
        return self._startY

    def getEndX(self):
        return self._endX

    def getEndY(self):
        return self._endY

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._startX = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'StartX')
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._startY = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'StartY')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._endX = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'EndX')
        elif parameterId == 4:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._endY = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'EndY')
        else:
            super(LinearSettingsElement, self).createChildForParameter(parameter)
