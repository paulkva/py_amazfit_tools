import logging
from watchFaceParser.config import Config

from watchFaceParser.models.gtr2.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.gtr2.elements.common.multilangImageElement import MultilangImageElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper


class FontRotateElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._x = None
        self._y = None
        self._radius = None
        self._rotateDirection = None

        super(FontRotateElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getRadius(self):
        return self._radius

    def getRotateDirection(self):
        return self._rotateDirection

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._x = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'X')
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._y = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Y')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._radius = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Radius')
        elif parameterId == 4:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._rotateDirection = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'RotateDirection')
        else:
            super(FontRotateElement, self).createChildForParameter(parameter)
