from watchFaceParser.elements.gts2mini.activityElements.separateDigits import ThreeDigits, FourDigits, FiveDigits

class ActivitySeparateDigits:
    definitions = {
        1: {'Name': 'Calories', 'Type': FourDigits},
        2: {'Name': 'Battery', 'Type': ThreeDigits},
        3: {'Name': 'Steps', 'Type': FiveDigits},
        4: {'Name': 'HeartRate', 'Type': FourDigits},
    }

