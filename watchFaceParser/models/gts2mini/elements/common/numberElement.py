import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper

class Box:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height


    def getX(self):
        return self._x


    def getY(self):
        return self._y


    def getWidth(self):
        return self._width


    def getHeight(self):
        return self._height


    def getLeft(self):
        return self._x


    def getRight(self):
        return self._x + self._width


    def getTop(self):
        return self._y


    def getBottom(self):
        return self._y + self._height


class NumberElement(ContainerElement):
    def __init__(self, parameter, parent, name):
        self._topLeftX = None
        self._topLeftY = None
        self._bottomRightX = None
        self._bottomRightY = None
        self._alignment = None
        self._spacing = 0
        self._paddingzero = False
        self._imageIndex = None
        self._imagesCount = None
        self._maxTextWidth = None
        self._box = None
        self._followxy = None
        super(NumberElement, self).__init__(None, parameter = parameter, parent = parent, name = name)

    def getBox(self):
        #return Box(self._topLeftX, self._topLeftY, self._bottomRightX - self._topLeftX, self._bottomRightY - self._topLeftY)
        return self._box


    def getAltBox(self, altCoordinates):
        return Box(altCoordinates._x, altCoordinates._y, self._bottomRightX - self._topLeftX, self._bottomRightY - self._topLeftY)

    def setBox(self, images, spacing, followxy):
        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)
        x = self._topLeftX if followxy is None else followxy[0]
        y = self._topLeftY if followxy is None else followxy[1]
        if bitmapWidth > self._maxTextWidth:
            self._box = Box(x, y, bitmapWidth, bitmapHeight)
        else:
            self._box = Box(x, y, self._maxTextWidth, bitmapHeight)
        return self._box

    def addTextWidth(self, width, spacing):
        if self._maxTextWidth > 0:
            if spacing > 0:
                self._maxTextWidth += spacing
        self._maxTextWidth += width

    def draw4(self, drawer, images, number, minimumDights = 1, force_padding = False, followxy = None):
        from watchFaceParser.helpers.drawerHelper import DrawerHelper

        print("NumberVor", number)
        if force_padding:
            self._paddingzero = True
        padding_length = 1
        if self._paddingzero:
            padding_length = minimumDights

        ar = self.getImagesForNumber(images, number, padding_length)
        self.setBox(ar, self._spacing, followxy)
        DrawerHelper.drawImages(drawer,
                                ar,
                                self._spacing,
                                self._alignment,
                                self._box)
        self._followxy = (self._box.getX() + self._box.getWidth() + 1, self._box.getY())
        return self._followxy

    def getImagesForNumber(self, images, number, minimumDigits = 1):
        self._maxTextWidth = 0
        stringNumber = str(number).zfill(minimumDigits)
        ar = []

        for digit in stringNumber:
            if int(digit) < self._imagesCount:
                imageIndex = self._imageIndex + int(digit)
                ar.append(images[imageIndex])
                self.addTextWidth(images[imageIndex].getBitmap().size[0], self._spacing)
        i = minimumDigits - len(stringNumber)
        while i > 0:
            self.addTextWidth(images[self._imageIndex].getBitmap().size[0], self._spacing)
            i = i - 1
        return ar


    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement

        parameterId = parameter.getId()
        if parameterId == 1:
            self._topLeftX = parameter.getValue()
            return ValueElement(parameter, self, 'TopLeftX')
        elif parameterId == 2:
            self._topLeftY = parameter.getValue()
            return ValueElement(parameter, self, 'TopLeftY')
        if parameterId == 3:
            self._bottomRightX = parameter.getValue()
            return ValueElement(parameter, self, 'BottomRightX')
        elif parameterId == 4:
            self._bottomRightY = parameter.getValue()
            return ValueElement(parameter, self, 'BottomRightY')
        elif parameterId == 5:
            self._alignment = parameter.getValue()
            return ValueElement(parameter, self, 'Alignment')
        elif parameterId == 6:
            self._spacing = parameter.getValue()
            return ValueElement(parameter, self, 'Spacing')
        elif parameterId == 7:
            self._paddingzero = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZero')
        elif parameterId == 8:
            self._imageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'ImageIndex')
        elif parameterId == 9:
            self._imagesCount = parameter.getValue()
            return ValueElement(parameter, self, 'ImagesCount')
        else:
            super(NumberElement, self).createChildForParameter(parameter)

