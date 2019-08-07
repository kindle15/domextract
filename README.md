# domextract
DOM based web content extractor for Japanese websites.

This tool extracts the article contents by using Random Forest.

## Preparation
You need to install MeCab.

```
git clone https://github.com/taku910/mecab && \
    cd mecab/mecab && \
    ./configure --enable-utf8-only && \
    make && \
    make check && \
    make install && \
    pip install --no-cache-dir mecab-python3 && \
    ldconfig && \
    cd ../mecab-ipadic && \
    ./configure --with-charset=utf8 && \
    make && \
    make install
```

## Installation

```
python setup.py install
```

## How to use

### 1. Extract from website.

```python
from domextract import Extractor
ext = Extractor()
result = ext.extract("http://example.com", is_url=True)
```

### 2. Extract from html file

```python
from domextract import Extractor
ext = Extractor()
result = ext.extract("./website.html", is_url=False)
```

### 3. Extract from html string

```python
import requests
from domextract import Extractor
r = requests.get("http://example.com")
data = r.content
ext = Extractor()
result = ext.extract(data, is_url=str)
```


## Test

You can test this module.

```
cd test
./run.sh
```

and the output should be this:

```
世界脊椎デー （せかいせきついデー、World Spine Day）は、 10月16日 に毎年実施されている、 脊椎 の健康・疾患の理解と予防を国際的に呼びかけることを目的とした 国際デー である [1] 。この国際デーは、 世界保健機関 （WHO）により2000年に立ち上げられた運動器の10年（BJD）の運動器活動週間の一環として世界中に広まっているキャンペーン。  世界脊椎デーは、2012年に運動器の10年（BJD）により制定され、 世界カイロプラクティック連合 (WFC)が中心となり世界的な学術団体から支援をされている。2012年以来、国内でのこの行事は世界カイロプラクティック連合の日本代表団体である 日本カイロプラクターズ協会 により行われている。世界脊椎デーにあわせて開発された、背筋を伸ばそう（Straighten Up）とまずは歩こう（Just Start Walking）プログラムは脊椎疾患を予防するための教育プログラムである。  運動器の10年（BJD）の運動器活動週間は、 10月12日  世界関節炎デー、 10月16日  世界脊椎デー、 10月17日  世界外傷デー、 10月19日  世界小児運動器デー、 10月20日 世界骨粗鬆症デー がある。 [
```

Node: It may occur some errors that based on zero division.

