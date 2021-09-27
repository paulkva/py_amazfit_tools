from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class PulseElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._image_number = None
        self._prefix = None
        self._nodata = None
        self._suffix = None
        self._icon = None
        super(PulseElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        followxy = (self._image_number.getTopLeftX(), self._image_number.getTopLeftY())

        if self._image_number:
            if self._prefix:
                temp = resources[self._prefix].getBitmap()
                drawer.paste(temp, (followxy[0], followxy[1]), temp)
                followxy = followxy[0] + temp.size[0], followxy[1]
            followxy = self._image_number.draw4(drawer,
                                                resources,
                                                state.getPulse(),
                                                minimumDights = 3,
                                                force_padding = False,
                                                followxy = followxy)
            if self._suffix and followxy:
                temp = resources[self._suffix].getBitmap()
                drawer.paste(temp, (followxy[0], followxy[1]), temp)
                followxy = followxy[0] + temp.size[0], followxy[1]
        if self._icon:
            self._icon.draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'ImageNumber')
            return self._image_number
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._prefix = parameter.getValue()
            return ValueElement(parameter, self, 'PrefixImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._nodata = parameter.getValue()
            return ValueElement(parameter, self, 'NoDataImageIndex')
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffix = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndex')
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._icon = ImageElement(parameter=parameter, parent=self, name='Icon')
            return self._icon
        elif parameterId == 6:  # Shortcut
            pass
        else:
            super(PulseElement, self).createChildForParameter(parameter)
