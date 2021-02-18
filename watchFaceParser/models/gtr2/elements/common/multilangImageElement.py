import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
from watchFaceParser.config import Config


class MultilangImageElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._landcode = None
        super(MultilangImageElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getLandCode(self):
        return self._landcode

    def setLandcode(self, landCode):
        self._landcode = landCode


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
        from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement

        parameterId = parameter.getId()

        if parameterId == 1:
            self._landcode = parameter.getValue()
            return ValueElement(parameter, self, 'LandCode')
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.imageSetElement import ImageSetElement
            self._ones = ImageSetElement(parameter, self, 'ImageSet')
            return self._ones
        else:
            super(MultilangImageElement, self).createChildForParameter(parameter)
