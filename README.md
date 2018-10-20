# domextract
DOM based web content extractor for Japanese websites

This tool can extract article body automatically by using Random Forest.


#preparation
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

# installation

```
python setup.py install
```

# example usage

A example usage is in test directory.

```
cd test
./run.sh
```

and the result is this:

```
世界脊椎デー （せかいせきついデー、World Spine Day）は、 10月16日 に毎年実施されている、 脊椎 の健康・疾患の理解と予防を国際的に呼びかけることを目的とした 国際デー である [1] 。この国際デーは、 世界保健機関 （WHO）により2000年に立ち上げられた運動器の10年（BJD）の運動器活動週間の一環として世界中に広まっているキャンペーン。  世界脊椎デーは、2012年に運動器の10年（BJD）により制定され、 世界カイロプラクティック連合 (WFC)が中心となり世界的な学術団体から支援をされている。2012年以来、国内でのこの行事は世界カイロプラクティック連合の日本代表団体である 日本カイロプラクターズ協会 により行われている。世界脊椎デーにあわせて開発された、背筋を伸ばそう（Straighten Up）とまずは歩こう（Just Start Walking）プログラムは脊椎疾患を予防するための教育プログラムである。  運動器の10年（BJD）の運動器活動週間は、 10月12日  世界関節炎デー、 10月16日  世界脊椎デー、 10月17日  世界外傷デー、 10月19日  世界小児運動器デー、 10月20日 世界骨粗鬆症デー がある。 [
```



