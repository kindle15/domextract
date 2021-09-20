# domextract
Web content extractor for articles.

## Preparation

```
sudo apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8
sudo ln -s /etc/mecabrc /usr/local/etc
```

## Installation

```
python setup.py install
```

## How to use

```bash
chrome --headless --disable-gpu --dump-dom http://example.com > test.html
```

```python3
import domextract

with open("test.html") as f:
    html = f.read()

ext = domextract.Extractor()
print(ext.extract(html))
```
