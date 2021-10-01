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

    def setWidth(self, width):
        self._width = width

    def getHeight(self):
        return self._height

    def setHeight(self, height):
        self._height = height

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
        self._imageIndex = None
        self._imagesCount = None
        self._maxTextWidth = None
        self._box = None
        self._followxy = None
        self._paddingzero = False
        super(NumberElement, self).__init__(None, parameter = parameter, parent = parent, name = name)

    def getTopLeftX(self):
        return self._topLeftX

    def getTopLeftY(self):
        return self._topLeftY

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
        if self._bottomRightX > self._box.getX() + self._box.getWidth():
            self._box.setWidth(self._bottomRightX - self._box.getX())
        if self._bottomRightY > self._box.getY() + self._box.getHeight():
            self._box.setHeight(self._bottomRightY - self._box.getY())
        return self._box

    def addTextWidth(self, width, spacing):
        if self._maxTextWidth > 0:
            if spacing > 0:
                self._maxTextWidth += spacing
        self._maxTextWidth += width

    def draw4(self, drawer, images, number, minimumDights = 1,
              force_padding = False, followxy = None, decimal_pointer = None, minus = None, prefix = None, suffix = None, delimiter_time = None):
        from watchFaceParser.helpers.drawerHelper import DrawerHelper

        if force_padding:
            self._paddingzero = True

        ar = self.getImagesForNumber(images, number, minimumDights, decimal_pointer, minus, prefix, suffix, delimiter_time)

        self.setBox(ar, self._spacing, followxy)

        DrawerHelper.drawImages(drawer,
                                ar,
                                self._spacing,
                                self._alignment,
                                self._box)

        self._followxy = (self._box.getX() + self._box.getWidth() + 1, self._box.getY())
        return self._followxy

    def getImagesForNumber(self, images, number, minimumDigits = 1, decimal_pointer = None, minus = None, prefix = None,
                           suffix = None, delimiter_time = None):
        padding_length = 1
        if self._paddingzero:
            padding_length = minimumDigits

        if number < 0:
            stringNumber = str(-number).zfill(padding_length)
        else:
            stringNumber = str(number).zfill(padding_length)

        self._maxTextWidth = 0
        ar = []
        if prefix:
            ar.append(images[prefix])
            self.addTextWidth(images[prefix].getBitmap().size[0], self._spacing)
        if number < 0 and minus:
            ar.append(images[minus])
            self.addTextWidth(images[minus].getBitmap().size[0], self._spacing)
        for digitIndex in range(len(stringNumber)):
            if decimal_pointer:
                if digitIndex == len(stringNumber)-1:
                    ar.append(images[decimal_pointer])
                    self.addTextWidth(images[decimal_pointer].getBitmap().size[0], self._spacing)
            if delimiter_time and digitIndex == len(stringNumber)-2:
                ar.append(images[delimiter_time])
                self.addTextWidth(images[delimiter_time].getBitmap().size[0], self._spacing)
            digit = stringNumber[digitIndex]
            if int(digit) < self._imagesCount:
                imageIndex = self._imageIndex + int(digit)
                ar.append(images[imageIndex])
                self.addTextWidth(images[imageIndex].getBitmap().size[0], self._spacing)
            if decimal_pointer:
                if digitIndex == len(stringNumber)-1:
                    break
        if suffix:
            ar.append(images[suffix])
            self.addTextWidth(images[suffix].getBitmap().size[0], self._spacing)

        print("Nik1", number, stringNumber, len(ar), self._maxTextWidth)
        i = minimumDigits - len(stringNumber)
        self.addTextWidth(images[self._imageIndex].getBitmap().size[0] * i, self._spacing)

        print("Nik2", number, stringNumber, len(ar), self._maxTextWidth)
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
            pass
        elif parameterId == 8:
            self._imageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'ImageIndex')
        elif parameterId == 9:
            self._imagesCount = parameter.getValue()
            return ValueElement(parameter, self, 'ImagesCount')
        else:
            super(NumberElement, self).createChildForParameter(parameter)

