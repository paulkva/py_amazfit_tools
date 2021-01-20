from watchFaceParser.elements.gtr2.multiLanguagePreview import MultiLanguagePreview 

class Background:
    definitions = {
        1: { 'Name': 'MultiLanguagePreview', 'Type': MultiLanguagePreview}, #add array support. LangCode 0 - 'zh' , 1 - 'zh-Hant' and 2 is for all languages
        2: { 'Name': 'BackgroundImageIndex', 'Type': 'long'}, 
    }