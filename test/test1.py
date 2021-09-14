import domextract

with open("test.html") as f:
    html = f.read()

ext = domextract.Extractor()
print(ext.extract(html))


