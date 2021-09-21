import re
import pickle
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup, Comment, Tag
from domextract.fe_dom import build, prepare_df
from domextract.xpath_soup import xpath_soup
from collections import namedtuple
import MeCab


def _get_textnodes(r, regex, regex0):
    soup = BeautifulSoup(r.content, "html.parser")
    [e.extract() for e in soup(text=lambda text: isinstance(text, Comment))]
    [e.extract() for e in soup.findAll(["script", "link", "noscript", "meta", "style"])]
    out = []
    arrived = set()
    for node in soup.findAll(["div","section","article"]):
        for n in node.findAll(text=True, recursive=True):
            if re.match(regex, n):
                continue
            xpath = xpath_soup(n)
            o = {"xpath":xpath, "#text":re.sub(regex0, ' ', str(n).replace("\n"," ").replace("\t"," "))}
            t = (o["xpath"], o["#text"])
            if t in arrived:
                continue
            arrived.add(t)
            out.append(o)
    df = pd.DataFrame(out)
    return df
    

def extract(target, model, columns, tagger, params, regex, regex0, regex1, regex2, threshold=0.35):
    r = namedtuple('Item',('content'))
    r.content = target
    df = _get_textnodes(r, regex, regex0)
    df = prepare_df(df, tagger)
    X = build(df, columns, *params)
    X = X.replace([np.inf, -np.inf], np.nan)
    X = X.fillna(0)
    probs = model.predict_proba(X)
    preds = [x[1]>threshold for x in probs]
    return ' '.join([re.sub(regex1, " ", re.sub(regex2, "", x)) for x,y in zip(df['#text'], preds) if y == True])


def prepare_data():
    import domextract
    from os.path import dirname, join
    path = dirname(domextract.__file__)
    fs = ["columns.txt", "rf_dom.pkl", "japanese", "english"]
    ps = [join(path, f) for f in fs]

    tagger = MeCab.Tagger("-Owakati")
    
    regex = re.compile(r"^[ \n\t]+$")
    regex0 = re.compile(r" [ ]+")
    regex1 = re.compile(r" [ ]+")
    regex2 = re.compile(r"[\r\n\t\u3000]")

    with open(ps[0]) as f:
        columns = [line.strip() for line in f]
    with open(ps[1], "rb") as f:
        clf = pickle.load(f)
    with open(ps[2]) as f:
        jpstps = [line.strip() for line in f]
    with open(ps[3]) as f:
        enstps = [line.strip() for line in f]

    plist = list(".,?!。！？、")
    nums = list("0123456789")
    endmark = list(".,?!。！？、")
    tags_b49 = "td div p tr table body ul span li blockquote b small a ol ul i form dl strong pre".split()
    tags_b110 = "a p td b li span i tr div strong em h3 h2 table h4 small sup h1 blockquote".split()        
        
    return clf, columns, tagger, (regex, regex0, regex1, regex2), (jpstps, enstps, plist, nums, endmark, tags_b49, tags_b110)
