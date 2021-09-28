import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement
from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement

class ShortcutElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._image = None
        super(ShortcutElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        self.draw2(drawer, resources, None)

    def draw2(self, drawer, images, angle, center=None):
        if self._image:
            self._image.draw2(drawer, images, angle, center)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._image = ImageElement(parameter = parameter, parent = self, name = 'Icon')
            return self._image
        elif parameterId == 2: # type, nothing to draw
            pass
        elif parameterId == 3: # element, nothing to draw
            pass
        else:
            return super(ShortcutElement, self).createChildForParameter(parameter)