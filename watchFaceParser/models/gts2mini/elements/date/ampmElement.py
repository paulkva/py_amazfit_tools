from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
import logging

class AmPmElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._common_x = None
        self._common_y = None
        self._image_index_am_cn = None
        self._image_index_pm_cn = None
        self._image_index_am_en = None
        self._image_index_pm_en = None
        self._coords_am = None
        self._coords_pm = None

        super(AmPmElement, self).__init__(parameters= None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        imageIndex = self._image_index_am_en if state.getTime().hour < 12 else self._image_index_pm_en

        temp = resources[imageIndex].getBitmap()

        if state.getTime().hour < 12:
            temp = resources[self._image_index_am_en].getBitmap()
            if self._coords_am:
                drawer.paste(temp, (self._coords_am.getX(), self._coords_am.getY()), temp)
            elif self._common_x and self._common_y:
                drawer.paste(temp, (self._common_x, self._common_y), temp)
        else:
            temp = resources[self._image_index_pm_en].getBitmap()
            if self._coords_pm:
                drawer.paste(temp, (self._coords_pm.getX(), self._coords_pm.getY()), temp)
            elif self._common_x and self._common_y:
                drawer.paste(temp, (self._common_x, self._common_y), temp)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        if parameterId == 1:
            self._common_x = parameter.getValue()
            return ValueElement(parameter=parameter, parent = self, name = 'CommonX')
        elif parameterId == 2:
            self._common_y = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='CommonY')
        elif parameterId == 3:
            self._image_index_am_cn = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='ImageIndexAMCN')
        elif parameterId == 4:
            self._image_index_pm_cn = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='ImageIndexPMCN')
        elif parameterId == 5:
            self._image_index_am_en = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='AmImageIndexEN')
        elif parameterId == 6:
            self._image_index_pm_en = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='PmImageIndexEN')
        elif parameterId == 7:
            pass
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._coords_am = CoordinatesElement(parameter=parameter, parent=self, name='CoordinatesAM')
            return self._coords_am
        elif parameterId == 9:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._coords_pm = CoordinatesElement(parameter=parameter, parent=self, name='CoordinatesPM')
            return self._coords_pm
        else:
            return super(AmPmElement, self).createChildForParameter(parameter)

