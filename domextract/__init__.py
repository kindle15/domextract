from domextract import dom_extract as de


class Extractor:

    def __init__(self):
        self.clf, self.columns, self.tagger, self.regex, self.params = de.prepare_data()
        
    def extract(self, html, threshold=0.35):
        return de.extract(html, self.clf, self.columns, self.tagger, self.params, *self.regex, threshold=threshold)
        
