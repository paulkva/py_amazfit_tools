import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
from watchFaceParser.config import Config
from watchFaceParser.utils.parametersConverter import toSigned32

class PointerScaleElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._center_x = None
        self._center_y = None
        self._range_from = None
        self._range_to = None
        self._pointer_image_index = None
        self._pointer_center_of_rotation_y = None
        super(PointerScaleElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw4(self, drawer, resources, value, total):
        assert(type(resources) == list)

        if value > total:
            value = total

        _startAngle = toSigned32(self._range_from) if self._range_from else 0
        _endAngle = toSigned32(self._range_to) if self._range_to else 360

        angle = 360 - _startAngle - int(value * (_endAngle - _startAngle) / total)

        bitmap = resources[self._pointer_image_index].getBitmap()
        (w, h) = bitmap.size
        offset_x = int(w / 2)
        offset_y = int(h / 2)
        if self._pointer_center_of_rotation_y:
            offset_y = self._pointer_center_of_rotation_y

        from PIL import Image

        temp = Image.new('RGBA', Config.getImageSize())
        temp.paste(bitmap, (Config.getImageSizeHalf()[0] - offset_x, Config.getImageSizeHalf()[1] - offset_y), bitmap)
        temp = temp.rotate(angle, resample=Image.BICUBIC)

        if self._center_x and self._center_y:
            drawer.paste(temp, (self._center_x - int(temp.size[0]/2), self._center_y- int(temp.size[1]/2)), temp)
        else:
            drawer.paste(temp, (0, 0), temp)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            self._center_x = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'CenterX')
        elif parameterId == 2:
            self._center_y = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'CenterY')
        elif parameterId == 3:
            self._range_from = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'RangeFrom')
        elif parameterId == 4:
            self._range_to = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'RangeTo')
        elif parameterId == 5:
            self._pointer_image_index = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'PointerImageIndex')
        elif parameterId == 6:
            self._pointer_center_of_rotation_y = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'PointerCenterOfRotationY')
        else:
            return super(PointerScaleElement, self).createChildForParameter(parameter)

