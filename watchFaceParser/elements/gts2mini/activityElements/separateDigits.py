from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet

class ThreeDigits:
    definitions = {
        2: { 'Name': 'Hundreds', 'Type': ImageSet},
        3: { 'Name': 'Tens', 'Type': ImageSet},
        4: { 'Name': 'Ones', 'Type': ImageSet},
        7: { 'Name': 'NoDataImage', 'Type': ImageSet},
    }

class FourDigits:
    definitions = {
        2: { 'Name': 'Thousands', 'Type': ImageSet},
        3: { 'Name': 'Hundreds', 'Type': ImageSet},
        4: { 'Name': 'Tens', 'Type': ImageSet},
        5: { 'Name': 'Ones', 'Type': ImageSet},
        7: { 'Name': 'NoDataImage', 'Type': ImageSet},
    }

class FiveDigits:
    definitions = {
        2: { 'Name': 'TenThousands', 'Type': ImageSet},
        3: { 'Name': 'Thousands', 'Type': ImageSet},
        4: { 'Name': 'Hundreds', 'Type': ImageSet},
        5: { 'Name': 'Tens', 'Type': ImageSet},
        6: { 'Name': 'Ones', 'Type': ImageSet},
        7: { 'Name': 'NoDataImage', 'Type': ImageSet},
    }
