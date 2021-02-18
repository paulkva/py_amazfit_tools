import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.config import Config


class MultilangImageCoordsElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._coordinates = None
        self._imageset = None
        super(MultilangImageCoordsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getCoordinates(self):
        return self._coordinates

    def getImageset(self):
        return self._imageset

    def draw3(self, drawer, resources, state):
        self.draw2(drawer, resources, None)


    def draw2(self, drawer, images, angle, center = None):
        x = self._x
        y = self._y

        if angle is None:
            temp = images[self._imageIndex].getBitmap()
            drawer.paste(temp, (x,y), temp)
        else:
            bitmap = images[self._imageIndex].getBitmap()
            from PIL import Image

            temp = Image.new('RGBA', Config.getImageSize())
            temp.paste(bitmap, (Config.getImageSizeHalf()[0] - x, Config.getImageSizeHalf()[1] - y), bitmap)
            temp = temp.rotate(angle)

            if center is None:
                drawer.paste(temp, (0,0), temp)
            else:
                drawer.paste(temp, (center.getX(),center.getY()), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates = CoordinatesElement(parameter, self, 'Coordinates')
            return self._coordinates
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.imageSetElement import ImageSetElement
            self._imageset = [ ImageSetElement(parameter = c, parent = self, name = 'ImageSet') for c in parameter.getChildren() ]
            return self._imageset
        else:
            super(MultilangImageCoordsElement, self).createChildForParameter(parameter)
