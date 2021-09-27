from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement


class ScaleElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._pointer_scale = None
        super(ScaleElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw4(self, drawer, resources, value, total):
        if self._pointer_scale:
            self._pointer_scale.draw4(drawer, resources, value, total)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.pointerScaleElement import PointerScaleElement
            self._pointer_scale = PointerScaleElement(parameter, self, 'PointerScale')
        else:
            super(ScaleElement, self).createChildForParameter(parameter)
