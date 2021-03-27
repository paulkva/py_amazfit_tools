import logging
from watchFaceParser.config import Config

from watchFaceParser.models.gtr2.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.gtr2.elements.common.multilangImageElement import MultilangImageElement
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


class ImageElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._x = None
        self._y = None
        self._noDataImageIndex = None
        self._multilangImage = []
        self._decimalPointImageIndex = None
        self._multilangImageUnit = []
        self._delimiterImageIndex = None
        self._multilangImageUnitMile = []
        self._maxTextWidth = None
        self._box = None
        self._followX = None
        super(ImageElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getNoDataImageIndex(self):
        return self._noDataImageIndex

    def getMultilangImage(self) -> [MultilangImageElement]:
        return self._multilangImage

    def getDecimalPointImageIndex(self):
        return self._decimalPointImageIndex

    def getMultilangImageUnit(self) -> [MultilangImageElement]:
        return self._multilangImageUnit

    def getDelimiterImageIndex(self):
        return self._delimiterImageIndex

    def getMultilangImageUnitMile(self) -> [MultilangImageElement]:
        return self._multilangImageUnitMile

    def getBox(self):
        return self._box

    def getFollowX(self):
        return self._followX

    def setBox(self, images, spacing, followX):
        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)
        x = self._x if followX is None else followX
        if bitmapWidth > self._maxTextWidth:
            self._box = Box(x, self._y, bitmapWidth, bitmapHeight)
        else:
            self._box = Box(x, self._y, self._maxTextWidth, bitmapHeight)
        return self._box


    def addTextWidth(self, width):
        self._maxTextWidth += width

    def draw4(self, drawer, images, number, alignment, spacing, paddingZero, displayFormAnalog, followX):
        if not alignment:
            alignment = 0
        if not paddingZero:
            paddingZero = 0
        if not spacing:
            spacing = 0
        if not displayFormAnalog:
            displayFormAnalog = False
        ar = self.getImagesForNumber(images, number, paddingZero, displayFormAnalog)
        self.setBox(ar, spacing, followX)
        self.drawImages(drawer, ar, spacing, alignment, self.getBox())
        self._followX = self._box.getX() + self._box.getWidth() + 1
        return self._followX

    def getImagesForNumber(self, images, number, paddingZero, displayFormAnalog):
        ar = []
        self._maxTextWidth = 0

        multilangImage = self.getImageForLand(2)
        multilangImageUnit = self.getImageUnitForLand(2)
        multilangImageUnitMile = self.getImageUnitMileForLand(2)
        minusSign = number[0] == "-"
        if minusSign:
            number = number[1:]

        if multilangImage:
            if displayFormAnalog:
                if int(number) <= multilangImage.getImageSet().getImagesCount():
                    imageIndex = multilangImage.getImageSet().getImageIndex() + int(number) - Config.getStartImageIndex() - 1
                    ar.append(images[imageIndex])
                    self.addTextWidth(images[imageIndex].getBitmap().size[0])
            else:
                if self.getDecimalPointImageIndex():
                    kilometers = int(int(number) / 1000)
                    decimals = int(int(number) % 1000 / 10)
                    ar.extend(self.getImagesForNumber2(images, str(kilometers), multilangImage, paddingZero - 2))
                    decimal_point_image_index = self.getDecimalPointImageIndex() - Config.getStartImageIndex()
                    ar.append(images[decimal_point_image_index])
                    self.addTextWidth(images[decimal_point_image_index].getBitmap().size[0])
                    ar.extend(self.getImagesForNumber2(images, str(decimals), multilangImage, 2))
                elif self.getDelimiterImageIndex():
                    delimiter_point_image_index = self.getDelimiterImageIndex() - Config.getStartImageIndex()
                    self.addTextWidth(images[delimiter_point_image_index].getBitmap().size[0])
                    if minusSign:
                        ar.append(images[delimiter_point_image_index])
                    ar.extend(self.getImagesForNumber2(images, number, multilangImage, paddingZero))
                else:
                    ar.extend(self.getImagesForNumber2(images, number, multilangImage, paddingZero))
        if multilangImageUnit:
            imageIndex = multilangImageUnit.getImageSet().getImageIndex() - Config.getStartImageIndex()
            ar.append(images[imageIndex])
            self.addTextWidth(images[imageIndex].getBitmap().size[0])
        elif multilangImageUnitMile:
            imageIndex = multilangImageUnitMile.getImageSet().getImageIndex() - Config.getStartImageIndex()
            ar.append(images[imageIndex])
            self.addTextWidth(images[imageIndex].getBitmap().size[0])

        return ar

    def getImagesForNumber2(self, images, stringNumber, multilangImage, paddingZero):
        ar = []
        for digit in stringNumber:
            if int(digit) < multilangImage.getImageSet().getImagesCount():
                imageIndex = multilangImage.getImageSet().getImageIndex() + int(digit) - Config.getStartImageIndex()
                ar.append(images[imageIndex])
                self.addTextWidth(images[imageIndex].getBitmap().size[0])
        if len(stringNumber) < paddingZero:
            self.addTextWidth(images[imageIndex].getBitmap().size[0] * ( paddingZero - len(stringNumber)) )
        return ar

    def getImageForLand(self, land = 0):
        if self._multilangImage:
            for i in self._multilangImage:
                if i.getLandCode() == land:
                    return i
            return self._multilangImage[0]
        return None

    def getImageUnitForLand(self, land = 0):
        if self._multilangImageUnit:
            for i in self._multilangImageUnit:
                if i.getLandCode() == land:
                    return i
            return self._multilangImageUnit[0]
        return None

    def getImageUnitMileForLand(self, land = 0):
        if self._multilangImageUnitMile:
            for i in self._multilangImageUnitMile:
                if i.getLandCode() == land:
                    return i
            return self._multilangImageUnitMile[0]
        return None

    @staticmethod
    def drawImages(drawer, images, spacing, alignment, box):
        assert(type(images) == list)
        assert(type(spacing) == int)
        assert(type(alignment) == int)

        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)

        from watchFaceParser.models.gtr2.textAlignment import TextAlignmentGTR2
        alignmentFlag = TextAlignmentGTR2(alignment)

        x = 0
        y = 0
        if alignmentFlag.hasFlag(TextAlignmentGTR2.Left):
            x = box.getX()
        elif alignmentFlag.hasFlag(TextAlignmentGTR2.Right):
            x = box.getRight() - bitmapWidth + 1
        else:
            x = (box.getLeft() + box.getRight() - bitmapWidth) >> 1

        y = box.getTop()

        if x < box.getLeft():
            x = box.getLeft()

        for image in images:
            temp = image.getBitmap()
            drawer.paste(temp, (x,y), temp)

            imageWidth = image.getBitmap().size[0]
            x += imageWidth + int(spacing)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._x = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'X')
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._y = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Y')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._noDataImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'NoDataImageIndex')
        elif parameterId == 4:
            self._multilangImage.append(MultilangImageElement(parameter, parent = self, name = 'MultilangImage'))
            return self._multilangImage
        elif parameterId == 5:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._decimalPointImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'DecimalPointImageIndex')
        elif parameterId == 6:
            self._multilangImageUnit.append(MultilangImageElement(parameter, parent = self, name = 'MultilangImageUnit'))
            return self._multilangImageUnit
        elif parameterId == 7:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._delimiterImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'DelimiterImageIndex')
        elif parameterId == 8:
            self._multilangImageUnitMile.append(MultilangImageElement(parameter, parent = self, name = 'MultilangImageUnitMile'))
            return self._multilangImageUnitMile
        else:
            super(ImageElement, self).createChildForParameter(parameter)
