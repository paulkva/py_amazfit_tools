import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement


class IconSetElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndex = None
        self._coordinates = None
        super(IconSetElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state, cursor = None):
        self.draw2(drawer, resources, state, cursor)


    def draw2(self, drawer, images, state = None, cursor = None):
        initial = 0
        if cursor == True:
            initial = state
        for i in range(initial, state + 1):
            x = self._coordinates[i]._x
            y = self._coordinates[i]._y
            temp = images[self._imageIndex + i].getBitmap()
            drawer.paste(temp, (x,y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameter.getId() == 1:
            self._imageIndex = parameter.getValue()
            if not self._imageIndex:
                self._imageIndex = 0
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'ImageIndex')
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates.append(CoordinatesElement(parameter, self, 'Coordinates'))
            return self._coordinates
        else:
            super(IconSetElement, self).createChildForParameter(parameter)