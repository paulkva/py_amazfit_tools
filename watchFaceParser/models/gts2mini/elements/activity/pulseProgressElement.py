import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class PulseProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circular = None
        self._image_progress = None
        self._iconsetprogress = None
        self._scale = None
        super(PulseProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        if self._image_progress:
            self._image_progress.draw4(drawer, resources, state.getPulse(), 220)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._image_progress = ImageSetElement(parameter=parameter, parent=self, name='ImageProgress')
            return self._image_progress
        elif parameterId == 3:
            pass
            # from watchFaceParser.models.gts2mini.elements.common.iconSetElement import IconSetElement
            # self._iconsetprogress = IconSetElement(parameter = parameter, parent = self, name ='IconSetProgress')
            # return self._iconsetprogress
        elif parameterId == 4:
            pass
        elif parameterId == 5:
            pass
        elif parameterId == 6:
            pass
            # from watchFaceParser.models.gts2mini.elements.common.scaleElement import ScaleElement
            # self._scale = ScaleElement(parameter = parameter, parent = self, name = '_scale')
            # return self._scale
        else:
            print ("Unknown PulseProgressElement",parameterId)
            return super(PulseProgressElement, self).createChildForParameter(parameter)
