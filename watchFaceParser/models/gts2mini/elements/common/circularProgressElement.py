import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement


class CircularProgressElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._centerX = None
        self._centerY = None
        self._radiusX = None
        self._radiusY = None
        self._startAngle = 0
        self._endAngle = 0
        self._width = 0
        self._color = None
        self._flatness = None
        self._imageIndex = None
        super(CircularProgressElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def draw4(self, drawer, resources, value, total):
        assert(type(resources) == list)
        assert(type(value) == int)
        assert(type(total) == int)
        if value > total:
            value = total
        sectorAngle = int(1.0 * (self._endAngle - self._startAngle) * value / total)

        #print ("_imageIndex",self._imageIndex)
        if self._imageIndex:
            temp = resources[self._imageIndex].getBitmap()
            from PIL import Image
            #mask = Image.new('RGBA',temp.size,self._color)
            mask = Image.new('RGBA',temp.size,(0,0,0,0))
			
            from PIL import ImageDraw
            d = ImageDraw.Draw(mask) # draw context
            radius = self._radiusY + int(self._width / 2) # patch for PIL arc
    		
            rect = (0, 0,
                int((radius  )*2) , int((radius )*2))
    
            d.arc(rect, start = -90 + self._startAngle, end = -90 + self._startAngle + sectorAngle, fill = self._color, width = self._width)

            if self._flatness == 180:
                #round edges
                import math
                x = int(temp.size[0] / 2 + (radius - self._width / 2) *math.cos(math.pi * (self._startAngle - 90)/180))
                y = int(temp.size[1] / 2 + (radius - self._width / 2) *math.sin(math.pi * (self._startAngle - 90)/180))
                d.ellipse((x- self._width / 2+1, y- self._width / 2+1, x+self._width/2-1, y+self._width/2-1), fill = self._color)
    
                x = int(temp.size[0] / 2 + (radius - self._width / 2) *math.cos(math.pi * (self._startAngle+ sectorAngle - 90)/180))
                y = int(temp.size[1] / 2 + (radius - self._width / 2) *math.sin(math.pi * (self._startAngle+ sectorAngle - 90)/180))
                d.ellipse((x- self._width / 2+1, y- self._width / 2+1, x+self._width/2-1, y+self._width/2-1), fill = self._color)
            elif self._flatness == 90:
                #spike
                import math
                x1 = int(temp.size[0] / 2 + (radius - self._width) *math.cos(math.pi * (self._startAngle - 90)/180))
                y1 = int(temp.size[1] / 2 + (radius - self._width) *math.sin(math.pi * (self._startAngle - 90)/180))
			    
                x2 = int(temp.size[0] / 2 + radius *math.cos(math.pi * (self._startAngle - 90)/180))
                y2 = int(temp.size[1] / 2 + radius *math.sin(math.pi * (self._startAngle - 90)/180))
			    
                x3 = int(temp.size[0] / 2 + (radius - self._width / 2) *math.cos(math.pi * (self._startAngle -self._width * 360 / (2*math.pi * (radius - self._width / 2)) - 90)/180))
                y3 = int(temp.size[1] / 2 + (radius - self._width / 2) *math.sin(math.pi * (self._startAngle -self._width * 360 / (2*math.pi * (radius - self._width / 2))- 90)/180))
                d.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = self._color)
			    
                x1 = int(temp.size[0] / 2 + (radius - self._width) *math.cos(math.pi * (self._startAngle+ sectorAngle - 90)/180))
                y1 = int(temp.size[1] / 2 + (radius - self._width) *math.sin(math.pi * (self._startAngle+ sectorAngle - 90)/180))
			    
                x2 = int(temp.size[0] / 2 + radius *math.cos(math.pi * (self._startAngle+ sectorAngle - 90)/180))
                y2 = int(temp.size[1] / 2 + radius *math.sin(math.pi * (self._startAngle+ sectorAngle - 90)/180))
			    
                x3 = int(temp.size[0] / 2 + (radius - self._width / 2) *math.cos(math.pi * (self._startAngle+ sectorAngle +self._width * 360 / (2*math.pi * (radius - self._width / 2)) - 90)/180))
                y3 = int(temp.size[1] / 2 + (radius - self._width / 2) *math.sin(math.pi * (self._startAngle+ sectorAngle +self._width * 360 / (2*math.pi * (radius - self._width / 2))- 90)/180))
                d.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = self._color)
            else:
                pass

            drawer.paste(temp, (self._centerX - self._radiusX - int(self._width  / 2), self._centerY - self._radiusY - int(self._width  / 2)), mask)

        else:
            from PIL import ImageDraw
            d = ImageDraw.Draw(drawer) # draw context
            radius = self._radiusX + int(self._width / 2) # patch for PIL arc
    		
            rect = (int(self._centerX - radius), int(self._centerY - radius),
                int(self._centerX + radius), int(self._centerY + radius))
    
            d.arc(rect, start = -90 + self._startAngle, end = -90 + self._startAngle + sectorAngle, fill = self._color, width = self._width)

            if self._flatness == 0:
                #round edges
                import math
                x = int(self._centerX + (radius - self._width / 2) *math.cos(math.pi * (self._startAngle - 90)/180))
                y = int(self._centerY + (radius - self._width / 2) *math.sin(math.pi * (self._startAngle - 90)/180))
                d.ellipse((x- self._width / 2+1, y- self._width / 2+1, x+self._width/2-1, y+self._width/2-1), fill = self._color)
			    
                x = int(self._centerX + (radius - self._width / 2) *math.cos(math.pi * (self._startAngle+ sectorAngle - 90)/180))
                y = int(self._centerY + (radius - self._width / 2) *math.sin(math.pi * (self._startAngle+ sectorAngle - 90)/180))
                d.ellipse((x- self._width / 2+1, y- self._width / 2+1, x+self._width/2-1, y+self._width/2-1), fill = self._color)
            elif self._flatness == 90:
                #spike
                import math
                x1 = int(self._centerX + (radius - self._width) *math.cos(math.pi * (self._startAngle - 90)/180))
                y1 = int(self._centerY + (radius - self._width) *math.sin(math.pi * (self._startAngle - 90)/180))
    
                x2 = int(self._centerX + radius *math.cos(math.pi * (self._startAngle - 90)/180))
                y2 = int(self._centerY + radius *math.sin(math.pi * (self._startAngle - 90)/180))
    
                x3 = int(self._centerX + (radius - self._width / 2) *math.cos(math.pi * (self._startAngle -self._width * 360 / (2*math.pi * (radius - self._width / 2)) - 90)/180))
                y3 = int(self._centerY + (radius - self._width / 2) *math.sin(math.pi * (self._startAngle -self._width * 360 / (2*math.pi * (radius - self._width / 2))- 90)/180))
                d.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = self._color)
    
                x1 = int(self._centerX + (radius - self._width) *math.cos(math.pi * (self._startAngle+ sectorAngle - 90)/180))
                y1 = int(self._centerY + (radius - self._width) *math.sin(math.pi * (self._startAngle+ sectorAngle - 90)/180))
    
                x2 = int(self._centerX + radius *math.cos(math.pi * (self._startAngle+ sectorAngle - 90)/180))
                y2 = int(self._centerY + radius *math.sin(math.pi * (self._startAngle+ sectorAngle - 90)/180))
    
                x3 = int(self._centerX + (radius - self._width / 2) *math.cos(math.pi * (self._startAngle+ sectorAngle +self._width * 360 / (2*math.pi * (radius - self._width / 2)) - 90)/180))
                y3 = int(self._centerY + (radius - self._width / 2) *math.sin(math.pi * (self._startAngle+ sectorAngle +self._width * 360 / (2*math.pi * (radius - self._width / 2))- 90)/180))
                d.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = self._color)
            elif self._flatness == 180:
                pass


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        if parameterId == 1:
            self._centerX = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'CenterX')
        elif parameterId == 2:
            self._centerY = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'CenterY')
        elif parameterId == 3:
            self._radiusX = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'RadiusX')
        elif parameterId == 4:
            self._radiusY = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'RadiusY')
        elif parameterId == 5:
            self._startAngle = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'StartAngle')
        elif parameterId == 6:
            self._endAngle = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'EndAngle')
        elif parameterId == 7:
            self._width = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Width')
        elif parameterId == 8:
            from resources.image.color import Color
            self._color = Color.fromArgb(0xff000000 | parameter.getValue())
            return ValueElement(parameter = parameter, parent = self, name = 'Color')
        elif parameterId == 9:
            self._flatness = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Flatness')
        elif parameterId == 10:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, 'ImageIndex')
        else:
            return super(CircularProgressElement, self).createChildForParameter(parameter)
