class Config:
    _deviceId = None
    _is_gtr = False
    _is_gts = False
    _is_trex = False
    _is_amazfitx = False
    _image_size = (360, 360)
    _preview_size = (210, 210)
    _autodetect = True

    _size_gtr_47 = (454, 454)
    _size_gtr_42 = (390, 390)
    _size_gts = (348,442)
    _size_amazfitx = (206,640)

    @staticmethod
    def setDeviceId(deviceId):
        Config._deviceId = deviceId
        if Config._autodetect:
            if deviceId == 0x20:
                print("Detected Verge Lite")
                Config.setVergeLiteMode(True)
            elif deviceId == 0x28:
                print("Detected GTR (47mm)")
                Config.setGtrMode(47)
            elif deviceId == 0x2a:
                print("Detected GTR (42mm)")
                Config.setGtrMode(42)
            elif deviceId == 0x2e:
                print("Detected GTS")
                Config.setGtsMode(True)
            elif deviceId == 0x34:
                print("Detected T-Rex")
                Config.setTrexMode(True)
            elif deviceId == 0x35:
                print("Detected AmazfitX")
                Config.setAmazfitXMode(True)

    @staticmethod
    def getDeviceId():
        return Config._deviceId

    @staticmethod
    def getAutodetect():
        return Config._autodetect

    @staticmethod
    def setXMode(isX):
        if isX:
            Config._autodetect = False
            Config._is_amazfitx = True
            Config._preview_size = (152, 472)


    @staticmethod
    def setGtrMode(gtr):
        Config._is_gtr = gtr
        if Config._is_gtr == 47:
            Config._autodetect = False
            Config._image_size = Config._size_gtr_47
            Config._preview_size = (266, 266)
        if Config._is_gtr == 42:
            Config._autodetect = False
            Config._image_size = Config._size_gtr_42
            Config._preview_size = (266, 266)

    @staticmethod
    def isGtrMode():
        return Config._is_gtr

    @staticmethod
    def isTrexMode():
        return Config._is_trex

    @staticmethod
    def isAmazfitXMode():
        return Config._is_amazfitx

    @staticmethod
    def setVergeLiteMode(vergelite):
        if vergelite:
            Config._autodetect = False

    @staticmethod
    def setTrexMode(trex):
        if trex:
            Config._autodetect = False
            Config._is_trex = 50

    @staticmethod
    def setAmazfitXMode(amazfitx):
        if amazfitx:
            Config._autodetect = False
            Config._is_amazfitx = 53
            Config._image_size = Config._size_amazfitx
            Config._preview_size = (152,472)

    @staticmethod
    def setGtsMode(gts):
        if gts:
            Config._autodetect = False
            Config._is_gts = 40
            Config._image_size = Config._size_gts
            Config._preview_size = (242,304)

    @staticmethod
    def isGtsMode():
        return Config._is_gts

    @staticmethod
    def getImageSize():
        return Config._image_size


    @staticmethod
    def getImageSizeHalf():
        return (int(Config._image_size[0] / 2),int(Config._image_size[1] / 2))


    @staticmethod
    def getPreviewSize():
        # return (Config._preview_size, Config._preview_size)
        return Config._preview_size

