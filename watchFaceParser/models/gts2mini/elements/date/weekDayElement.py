import logging

from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement

class WeekDayElement(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        super(WeekDayElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        import locale
        nl = locale.getdefaultlocale()
        offset = 0
        if len(nl)>0 and isinstance(nl[0], str) and not nl[0].startswith('zh') and self.getImagesCount()==21:
            offset = 14
        if len(nl)>0 and isinstance(nl[0], str) and not nl[0].startswith('zh') and self.getImagesCount()==14:
            offset = 7
        super(WeekDayElement, self).draw3(drawer, resources, state.getTime().weekday() + offset)
