import logging

from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement

class ImagesElement(ImageSetElement):

    def __init__(self, parameter, parent, name = None):
        super(ImagesElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
#        print("wether ImageElement draw",state)
        super(ImagesElement, self).draw3(drawer, resources, state)
