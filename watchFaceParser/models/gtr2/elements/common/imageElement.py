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
        self._followxy = None
        super(ImageElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def getX(self):
        return 0 if self._x is None else self._x

    def getY(self):
        return 0 if self._y is None else self._y

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

    def getFollowXY(self):
        return self._followxy

    def setBox(self, images, spacing, followxy):
        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)
        x = self.getX() if followxy is None else followxy[0]
        y = self.getY() if followxy is None else followxy[1]
        if bitmapWidth > self._maxTextWidth:
            self._box = Box(x, y, bitmapWidth, bitmapHeight)
        else:
            self._box = Box(x, y, self._maxTextWidth, bitmapHeight)
        return self._box


    def addTextWidth(self, width, spacing):
        if self._maxTextWidth > 0:
            self._maxTextWidth += spacing
        self._maxTextWidth += width

    def draw4(self, drawer, images, number, alignment, spacing,
              paddingZero, paddingZeroDigits, paddingZeroLength, displayFormAnalog, followxy):
        if number is None: return
        
        if not alignment:
            alignment = 0
        if not paddingZero:
            paddingZero = 0
        if not spacing:
            spacing = 0
        if not displayFormAnalog:
            displayFormAnalog = False
        ar = self.getImagesForNumber(images, number, alignment, spacing, paddingZero, paddingZeroDigits, paddingZeroLength, displayFormAnalog)
        self.setBox(ar, spacing, followxy)
        self.drawImages(drawer, ar, spacing, alignment, self.getBox())
        self._followxy = (self._box.getX() + self._box.getWidth() + 1, self._box.getY())
        return self._followxy

    def getImagesForNumber(self, images, number, alignment, spacing, paddingZero, paddingZeroDigits, paddingZeroLength, displayFormAnalog):
        ar = []
        self._maxTextWidth = 0

        multilangImage = self.getImageForLand(2)
        multilangImageUnit = self.getImageUnitForLand(2)
        multilangImageUnitMile = self.getImageUnitMileForLand(2)
        minusSign = number < 0
        number = abs(number)

        if multilangImage:
            if displayFormAnalog:
                if int(number) <= multilangImage.getImageSet().getImagesCount():
                    imageIndex = multilangImage.getImageSet().getImageIndex() + \
                                 int(number) - Config.getStartImageIndex() - 1
                    ar.append(images[imageIndex])
                    self.addTextWidth(images[imageIndex].getBitmap().size[0], spacing)
            else:
                if self.getDecimalPointImageIndex():
                    kilometers = int(int(number) / 1000)
                    decimals = int(int(number) % 1000 / 10)
                    ar.extend(self.getImagesForNumber2(
                        images, kilometers, multilangImage, alignment, spacing, paddingZero, paddingZeroDigits - 2, paddingZeroLength - 2))
                    decimal_point_image_index = self.getDecimalPointImageIndex() - Config.getStartImageIndex()
                    ar.append(images[decimal_point_image_index])
                    self.addTextWidth(images[decimal_point_image_index].getBitmap().size[0], spacing)
                    ar.extend(self.getImagesForNumber2(images, str(decimals), multilangImage, alignment, spacing, paddingZero, 2, 2))
                elif self.getDelimiterImageIndex():
                    delimiter_point_image_index = self.getDelimiterImageIndex() - Config.getStartImageIndex()
                    self.addTextWidth(images[delimiter_point_image_index].getBitmap().size[0], spacing)
                    if minusSign:
                        ar.append(images[delimiter_point_image_index])
                    ar.extend(self.getImagesForNumber2(images, number, multilangImage, alignment, spacing, paddingZero, paddingZeroDigits, paddingZeroLength))
                else:
                    ar.extend(self.getImagesForNumber2(images, number, multilangImage, alignment, spacing, paddingZero, paddingZeroDigits, paddingZeroLength))
        if multilangImageUnit:
            imageIndex = multilangImageUnit.getImageSet().getImageIndex() - Config.getStartImageIndex()
            ar.append(images[imageIndex])
            self.addTextWidth(images[imageIndex].getBitmap().size[0], spacing)
        elif multilangImageUnitMile:
            imageIndex = multilangImageUnitMile.getImageSet().getImageIndex() - Config.getStartImageIndex()
            ar.append(images[imageIndex])
            self.addTextWidth(images[imageIndex].getBitmap().size[0], spacing)

        return ar

    def getImagesForNumber2(self, images, number, multilangImage, alignment, spacing, paddingZero, paddingZeroDigits, paddingZeroLength):
        ar = []

        imageIndex = multilangImage.getImageSet().getImageIndex() - Config.getStartImageIndex()
        stringNumber = str(number)
        if paddingZero:
            stringNumber = stringNumber.zfill(paddingZeroDigits)

        for digit in stringNumber:
            if int(digit) < multilangImage.getImageSet().getImagesCount():
                imageIndex = multilangImage.getImageSet().getImageIndex() + int(digit) - Config.getStartImageIndex()
                ar.append(images[imageIndex])
                self.addTextWidth(images[imageIndex].getBitmap().size[0], spacing)
        i = paddingZeroLength - len(stringNumber)
        while i > 0:
            self.addTextWidth(images[imageIndex].getBitmap().size[0], spacing)
            i = i - 1
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

        print(alignment, box.getLeft(), box.getTop(), box.getRight(), box.getBottom(), bitmapWidth, bitmapHeight)

        x = 0
        y = 0
        if alignment == 0 or alignment is None:
            x = box.getX()
        elif alignment == 2:
            x = box.getRight() - bitmapWidth + 1
        else:
            x = (box.getLeft() + box.getRight() - bitmapWidth) >> 1

        y = box.getTop()

        if x < box.getLeft():
            x = box.getLeft()

        for image in images:
            temp = image.getBitmap()
            print('x', x, 'y', y, 'box', box.getLeft())
            drawer.paste(temp, (x, y), temp)

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
