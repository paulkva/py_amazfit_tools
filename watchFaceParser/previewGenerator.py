from watchFaceParser.config import Config

class PreviewGenerator:
    @staticmethod
    def createAnimation(descriptor, images, states):
        if not Config.isOldFormat() and (Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode()  or Config.isGts2MiniMode()): 
            from watchFaceParser.models.gtr2.elements.watchFace import WatchFace
        else:
            from watchFaceParser.models.elements.watchFace import WatchFace

        previewWatchFace = WatchFace(descriptor)
        for watchState in states:
            image = PreviewGenerator.createFrame(previewWatchFace, images, watchState)
            yield image


    @staticmethod
    def createImage(descriptor, images, state):
        if not Config.isOldFormat() and (Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode()  or Config.isGts2MiniMode()): 
            from watchFaceParser.models.gtr2.elements.watchFace import WatchFace
        else:
            from watchFaceParser.models.elements.watchFace import WatchFace
                    
        previewWatchFace = WatchFace(descriptor)
        return PreviewGenerator.createFrame(previewWatchFace, images, state)


    @staticmethod
    def createFrame(watchFace, resources, state):
        from PIL import Image, ImageDraw

        graphics = Image.new('RGBA', Config.getImageSize())
        watchFace.draw3(graphics, resources, state)
        return graphics
