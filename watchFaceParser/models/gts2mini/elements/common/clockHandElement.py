import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
from watchFaceParser.config import Config

class ClockHandElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndex = None
        self._pointer_center_of_rotation_y = None
        self._center = None
        self._centerImage = None
        super(ClockHandElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw4(self, drawer, resources, value, total):
        assert(type(resources) == list)

        _startAngle = 0
        _endAngle = 360

        angle = 360 - _startAngle - int(value * (_endAngle - _startAngle) / total)

        #self._image.draw2( drawer, resources, angle, self._center)

        bitmap = resources[self._imageIndex].getBitmap()
        (w, h) = bitmap.size
        offset_x = int(w/2)
        offset_y = int(h/2)
        if self._pointer_center_of_rotation_y:
            offset_y = self._pointer_center_of_rotation_y

        from PIL import Image

        temp = Image.new('RGBA', Config.getImageSize())
        temp.paste(bitmap, (Config.getImageSizeHalf()[0] - offset_x, Config.getImageSizeHalf()[1] - offset_y), bitmap)
        temp = temp.rotate(angle, resample=Image.BICUBIC)

        if self._center is None:
            drawer.paste(temp, (0, 0), temp)
        else:
            drawer.paste(temp, (self._center.getX() - int(temp.size[0]/2), self._center.getY()- int(temp.size[1]/2)), temp)

        if self._centerImage:
            #angle = 360 - _startAngle - int(value * (_endAngle - _startAngle) / total)
            self._centerImage.draw2(drawer, resources, None)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'ImageIndex')
        elif parameterId == 2:
            self._pointer_center_of_rotation_y = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'PointerCenterOfRotationY')
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._center = CoordinatesElement(parameter=parameter, parent=self, name='CenterCoordinates')
            return self._center
        if parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._centerImage = ImageElement(parameter = parameter, parent = self, name = 'CoverImage')
            return self._centerImage
        else:
            return super(ClockHandElement, self).createChildForParameter(parameter)

