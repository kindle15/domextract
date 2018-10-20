from domextract import dom_extract as de


class Extractor:

    def __init__(self):
        self.clf, self.columns, self.tagger, self.regex, self.params = de.prepare_data()
        
    def extract(self, url, threshold=0.35, is_url=True, debug=False):
        return de.extract(url, self.clf, self.columns, self.tagger, self.params, *self.regex, threshold=threshold, is_url=is_url, debug=debug)
        
