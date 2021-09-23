from watchFaceParser.elements.gts2mini.statusElements.switch import Switch

class Status:
    definitions = {
        1: { 'Name': 'DoNotDisturb', 'Type': Switch},
        2: { 'Name': 'Lock', 'Type': Switch},
        3: { 'Name': 'Bluetooth', 'Type': Switch},
        4: { 'Name': 'Alarm', 'Type': Switch},
    }

