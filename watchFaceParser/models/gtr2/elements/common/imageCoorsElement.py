import logging

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class ImageCoordsElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._coordinates = None
        self._imageIndex = None
        self._imageIndex2 = None
        self._imageIndex3 = None
        super(ImageCoordsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getCoordinates(self):
        return self._coordinates

    def getImageIndex(self):
        return self._imageIndex

    def getImageIndex2(self):
        return self._imageIndex2

    def getImageIndex3(self):
        return self._imageIndex3

    def draw3(self, drawer, resources, state):
        image_index = self.getImageIndex()-1
        temp = resources[image_index].getBitmap()
        drawer.paste(temp, (self.getCoordinates().getX(), self.getCoordinates().getY()), temp)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates = CoordinatesElement(parameter, self, 'Coordinates')
            return self._coordinates
        elif parameter.getId() == 2:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
        elif parameter.getId() == 3:
            self._imageIndex2 = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex2?')
        elif parameter.getId() == 4:
            self._imageIndex3 = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex3?')
        else:
            super(ImageCoordsElement, self).createChildForParameter(parameter)
