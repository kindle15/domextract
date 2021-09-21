from domextract import dom_extract as de


class Extractor:
    def __init__(self):
        x = de.prepare_data()
        self.clf = x[0]
        self.columns = x[1]
        self.tagger = x[2]
        self.regex = x[3]
        self.params = x[4]

    def extract(self, html, threshold=0.35):
        return de.extract(html,
                          self.clf,
                          self.columns,
                          self.tagger,
                          self.params,
                          *self.regex,
                          threshold=threshold)
