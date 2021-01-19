from watchFaceParser.elements.multiLanguagePreviewImage import MultiLanguagePreviewImage

class MultiLanguagePreview:
    definitions = {
        1: { 'Name': 'LangCode', 'Type':'long'},
        2: { 'Name': 'Image', 'Type': MultiLanguagePreviewImage}, 
    }