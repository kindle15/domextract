import domextract
import requests

ext = domextract.Extractor()
print(ext.extract("test.html",is_url=False, debug=True))


