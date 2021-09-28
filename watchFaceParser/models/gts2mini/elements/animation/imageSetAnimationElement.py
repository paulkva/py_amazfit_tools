from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class ImageSetAnimationElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._image_progress = None
        self._frame_interval = None
        self._play_times = None
        self._repeat = False
        super(ImageSetAnimationElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):

        if self._image_progress:
            animationindex = state.getAnimation()
            print("Animation", animationindex)

            if animationindex > self._image_progress.getImagesCount() - 1:
                if self._repeat:
                    while animationindex > self._image_progress.getImagesCount() - 1:
                        animationindex = animationindex - self._image_progress.getImagesCount() 
                    print("Animation endindex", animationindex)
                    self._image_progress.draw3(drawer, resources, animationindex)
            else:
                self._image_progress.draw3(drawer, resources, animationindex)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._image_progress = ImageSetElement(parameter=parameter, parent=self, name='ImageProgress')
            return self._image_progress
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._frame_interval = parameter.getValue()
            return ValueElement(parameter, self, 'FrameInterval')
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._play_times = parameter.getValue()
            return ValueElement(parameter, self, 'PlayTimes')
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._repeat = parameter.getValue()
            return ValueElement(parameter, self, 'Repeat')
        else:
            super(ImageSetAnimationElement, self).createChildForParameter(parameter)
