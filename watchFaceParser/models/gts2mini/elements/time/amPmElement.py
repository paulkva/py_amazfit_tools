from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
import logging
#import locale

class AmPmElement(CoordinatesElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndexAmCn = None
        self._imageIndexPmCn = None
        self._imageIndexAmEn = None
        self._imageIndexPmEn = None
        super(AmPmElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def getImageIndexAmCn(self):
        return self._imageIndexAmCn

    def getImageIndexPmCn(self):
        return self._imageIndexPmCn

    def getImageIndexAmEn(self):
        return self._imageIndexAmEn

    def getImageIndexPmEn(self):
        return self._imageIndexPmEn


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        #nl = locale.getdefaultlocale()
        imageIndex = self.getImageIndexAmCn() if state.getTime().hour < 12 else self.getImageIndexPmCn()
        #if len(nl)>0:
        #    if not nl[0].startswith('zh'):
        #        imageIndex += 2
        temp = resources[imageIndex].getBitmap()

        if self._parent.getPm() and state.getTime().hour >= 12:
            drawer.paste(temp, (self._parent.getPm().getX(), self._parent.getPm().getY()), temp)
        else:
            drawer.paste(temp, (self._x, self._y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 3:
            self._imageIndexAmCn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexAmCn')
        elif parameterId == 4:
            self._imageIndexPmCn = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexPmCn')
        #elif parameterId == 5:
        #    self._imageIndexAmCn = parameter.getValue()
        #    return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexAmEn')
        #elif parameterId == 6:
        #    self._imageIndexPmCn = parameter.getValue()
        #    return ValueElement(parameter = parameter, parent = self, name = 'ImageIndexPmEn')
        else:
            return super(AmPmElement, self).createChildForParameter(parameter)

