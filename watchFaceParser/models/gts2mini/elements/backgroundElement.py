import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement
from watchFaceParser.config import Config
from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
from resources.image.color import Color

class BackgroundElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._image = None
        self._color = None
        self._floating = None
        super(BackgroundElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getBackgroundImageIndex(self):
        return self._image

    def getColor(self):
        return self._color

    def draw3(self, drawer, resources, state):
        self.draw2(drawer, resources, None)

    def draw2(self, drawer, images, angle, center=None):
        x = 0
        y = 0

        from PIL import ImageDraw, Image

        if self._image is None:
            if self._color is None:
                self._color = Color.fromArgb(0xff000000)
            size = Config.getImageSize()
            d = ImageDraw.Draw(drawer)
            d.rectangle([(x, y), size], fill=self.getColor())
        else:
            self._image.draw2(drawer, images, angle, center)

        if self._floating:
            self._floating.draw2(drawer, images, angle, center)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._image = ImageElement(parameter = parameter, parent = self, name = 'Image')
            return self._image
        elif parameterId == 2: # color
            self._color = Color.fromArgb(0xff000000 | parameter.getValue())
            return ValueElement(parameter = parameter, parent = self, name = 'BackgroundColor')
        elif parameterId == 3: # Preview
            pass
        elif parameterId == 4: # Preview Korean
            pass
        elif parameterId == 5: # Preview Chinese
            pass
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._floating = ImageElement(parameter=parameter, parent=self, name='FloatingLayer')
            return self._floating
        else:
            return super(BackgroundElement, self).createChildForParameter(parameter)