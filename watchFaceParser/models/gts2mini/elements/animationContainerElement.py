import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class AnimationContainerElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._imageset = []
        super(AnimationContainerElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        if self._imageset:
            for a in self._imageset:
                a.draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.animation.imageSetAnimationElement import ImageSetAnimationElement
            self._imageset.append(ImageSetAnimationElement(parameter = parameter, parent = self, name = 'ImageSetAnimation'))
            return self._imageset
        else:
            return super(AnimationContainerElement, self).createChildForParameter(parameter)

