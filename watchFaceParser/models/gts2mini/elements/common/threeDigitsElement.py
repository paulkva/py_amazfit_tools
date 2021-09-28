import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement


class ThreeDigitsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._tens = None
        self._ones = None
        self._hundreds = None
        super(ThreeDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getTens(self):
        return self._tens

    def getOnes(self):
        return self._ones

    def getHundreds(self):
        return self._hundreds

    def draw4(self, drawer, images, number, padding_zero = False):
        assert(type(images) == list)
        assert(type(number) == int)

        if number > 999:
            number = number % 1000

        if self.getOnes():
            if padding_zero or int(number / 100) > 0:
                self.getOnes().draw3(drawer, images, int(number / 100))
        if self.getTens():
            if padding_zero or (int(number / 100) > 0 or int(number % 100 / 10)):
                self.getTens().draw3(drawer, images, int(number % 100 / 10))
        if self.getHundreds():
            self.getHundreds().draw3(drawer, images, int(number % 100 % 10))

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            pass
        if parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._hundreds = ImageSetElement(parameter, self, 'Hundreds')
            return self._hundreds
        if parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._tens = ImageSetElement(parameter, self, 'Tens')
            return self._tens
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._ones = ImageSetElement(parameter, self, 'Ones')
            return self._ones
        else:
            super(ThreeDigitsElement, self).createChildForParameter(parameter)
