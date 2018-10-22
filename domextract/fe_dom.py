import re
import pandas as pd
import MeCab
import string
import numpy as np


def load_stopwords(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f]


def tokenize(x, tagger):
    return tagger.parse(x).split()


def prepare_df(df, tagger):
    from functools import partial
    reg = re.compile(r"\[[0-9]+\]")
    df['xpath_fixed'] = list(map(lambda x: re.sub(reg,"",x),df['xpath'].tolist()))
    df = df[list(map(lambda x: "script" not in x, df['xpath_fixed']))]
    df['#text_tokenized'] = list(map(partial(tokenize, tagger=tagger), df["#text"]))
    return df


def b1(df, column="#text"):
    return df[[column]].duplicated()


def b3_single(xpath_series, xpath_fixed, length):
    return sum(xpath_series == xpath_fixed)/length


def b5_single(tokenized):
    return np.log(len(tokenized))


def b6_single(tokenized):
    return np.mean([len(y) for y in tokenized])


def b7_single(tokenized, jpstps, enstps):
    tmp = np.isin(tokenized, jpstps+enstps)
    if len(tmp) == 0:
        return 0
    else:
        return float(sum(tmp))/float(len(tmp))


def b9_single(text):
    return np.log(len(list(text)))


def o4_single(xpath_fixed):
    return "p" in xpath_fixed.split("/")


def b10_b24_single(text, plist):
    tmp = np.isin(list(text), plist)
    t = float(sum(tmp))
    n_punkt = t
    if len(tmp) == 0:
        punkt_ratio = 0
    else:   
        punkt_ratio = np.log(float(t) / float(len(tmp)))
    return punkt_ratio, n_punkt


def b11_single(text, nums):
    tmp = list(text)
    if len(tmp) == 0:
        num_ratio = 0
    else:
        num_ratio = float(sum(np.isin(tmp,nums)))/float(len(tmp))
    return num_ratio


def b14_single(text, endmark):
    return np.any([text.strip().endswith(y) for y in endmark])


def b26_single(n, length):
    return float(n)/float(length)


def b29p_single(text, target, col2):
    try:
        b29 = float(len(list(text)))/float(sum(len(list(y)) for y in target[col2]))
    except:
        b29 = 0
    return b29


def update_b29p(b29, parent_level):
    if parent_level == 1:
        return {'b29': b29}
    elif parent_level == 2:
        return {'b70': b29}
    elif parent_level == None:
        return {'b90': b29}
    return pf

def get_parent(x, parent_level):
    if parent_level==None:
        parent = "/html/body"
    else:
        parent = '/'.join(x.split("/")[:-parent_level])
    return parent


def b30p_single(target, col3):
    atags = [y.endswith("a") for y in target[col3]]
    if len(atags) == 0:
        b30 = 0
    else:
        b30 = float(sum(atags))/float(len(atags))
    return b30


def o1p_single(target, col3):   
    ptags = ["p" in y.split("/") for y in target[col3]]
    if len(ptags) == 0:
        o1 = 0
    else:
        o1 = float(sum(ptags))/float(len(ptags))
    return o1


def b7p_single(target, col4, jpstps, enstps):
    b7 = []
    for y in target[col4]:
        tmp = np.isin(y, jpstps+enstps)
        b7.append(tmp)
    b7 = np.concatenate(b7)
    if len(b7) == 0:
        b7 = 0
    else:
        b7 = float(sum(b7))/float(len(b7))
    return b7


def b10p_single(target, col2, plist):
    punkt_ratio = []
    tmp = []
    for y in target[col2]:
        tmp.append(np.isin(list(y), plist))
    t = sum(np.concatenate(tmp))
    if len(tmp) == 0:
        punkt_ratio = 0.0
    else:   
        punkt_ratio = np.log(
            float(t) / float(len(tmp))
        )
    return punkt_ratio

def b11p_single(target, col2, nums):
    num_ratio = []
    tmp = []
    for y in target[col2]:
        tmp += list(y)
    if len(tmp) == 0:
        num_ratio = 0
    else:
        num_ratio = float(sum(np.isin(tmp,nums)))/float(len(tmp))
    return num_ratio


def update_pf(pf, parent, parent_level, values):
    if parent_level == 1:
        keys = ['b31', 'b32', 'b34', 'b35', 'b36', 'b39', 'b29','b30', 'o1']
    elif parent_level == 2:
        keys = ['b72', 'b73', 'b75', 'b76', 'b77', 'b80', 'b70', 'b71', 'o2']
    elif parent_level == None:
        keys = ['b92', 'b93', 'b95', 'b96', 'b97', 'b100', 'b90', 'b91', 'o3']
    assert len(keys) == len(values)
    pf[parent] = dict(zip(keys, values))
    return pf
    
        
def b29_b30_o1_b31_single(pf, tdict, df, x, text, rdata, col1="xpath", col2="#text", col3="xpath_fixed", col4="#text_tokenized", parent_level=1):
    jpstps = rdata["jpstps"]
    enstps = rdata["enstps"]
    plist = rdata["plist"]
    nums = rdata["nums"]
    endmark = rdata["endmark"]
    parent = get_parent(x, parent_level)

    if parent in pf:
        try:
            target = tdict[parent]
            b29 = b29p_single(text, target, col2)
            b29 = update_b29p(b29, parent_level)
            return parent, pf, tdict, b29
        except:
            pass
    target = df[list(map(lambda y: parent in y, df[col1]))]
    b29 = b29p_single(text, target, col2)
    b29 = update_b29p(b29, parent_level)
    b30 = b30p_single(target, col3)
    o1 = o1p_single(target, col3)
    b6 = np.mean(np.concatenate([[len(y) for y in x] for x in target[col4]]))
    b7 = b7p_single(target, col4, jpstps, enstps)
    b9 = np.log(len(list(' '.join([y for y in target[col2]]))))
    b10 = b10p_single(target, col2, plist)
    b11 = b11p_single(target, col2, nums)
    b14 = np.any([target[col2].tolist()[-1].endswith(y) for y in endmark])
    values = [b6, b7, b9, b10, b11, b14, b29, b30, o1]
    pf = update_pf(pf, parent, parent_level, values)
    tdict[parent] = target
    return parent, pf, tdict, b29


def b49_single(xpath_fixed, tags, parent_level=1):
    tmp = np.zeros(len(tags))
    t = xpath_fixed.split("/")[-(parent_level+1)]
    try:
        ind = tags.index(t)
        tmp[ind] = 1.0
    except:
        pass
    return {str(k):v for k,v in zip(range(49, 49+len(tags)), tmp)}


def b110_single(xpath_fixed, tags):    
    tmp = np.zeros(len(tags))
    t = xpath_fixed.split("/")[-1]
    try:
        ind = tags.index(t)
        tmp[ind] = 1.0
    except:
        pass
    return {str(k):v for k,v in zip(range(110, 110+len(tags)), tmp)}


def execute(d):
    n = d[0]
    t, x, xf, tt = d[1]
    length = d[2]
    pf, gpf, rpf, tdict, gtdict, rtdict = d[3],d[4],d[5],d[6],d[7],d[8]
    df = d[9]
    xfser = d[10]
    jpstps = d[11]
    enstps = d[12]
    nums = d[13]
    plist = d[14]
    endmark = d[15]
    tags_b49 = d[16]
    tags_b110 = d[17]
    rdata = {"plist":plist, "nums":nums, "endmark":endmark, "jpstps":jpstps, "enstps":enstps}    
    b10, b24 = b10_b24_single(t, plist)
    parent, pf, tdict, b29_1 = b29_b30_o1_b31_single(pf, tdict, df, x, t, rdata, parent_level=1)
    gparent, gpf, gtdict, b29_2 = b29_b30_o1_b31_single(gpf, gtdict, df, x, t, rdata, parent_level=2)
    rparent, rpf, rtdict, b29_3 = b29_b30_o1_b31_single(rpf, rtdict, df, x, t, rdata, parent_level=None)
    ptag = b49_single(xf, tags_b49)
    ctag = b110_single(xf, tags_b110)
    
    data = {
        "b3": b3_single(xfser, xf, length),
        "b5": b5_single(tt),
        "b6": b6_single(tt),
        "b7": b7_single(tt, jpstps, enstps),
        "b9": b9_single(t),
        "o4": o4_single(xf),
        "b10": b10,
        "b24": b24,
        "b11": b11_single(t, nums),
        "b14": b14_single(t, endmark),
        "b26": b26_single(n, length),
        **pf[parent],
        **gpf[gparent],
        **rpf[rparent],
        **ptag,
        **ctag,
        **b29_1,
        **b29_2,
        **b29_3
    }
    return data


def build(df, columns, jpstps, enstps, plist, nums, endmark,tags_b49,tags_b110, is_multiprocess=False, col1="#text", col2="xpath", col3="xpath_fixed", col4="#text_tokenized"):
    tser, xser, xfser, ttser = df[col1], df[col2], df[col3], df[col4]
    assert len(tser) == len(xser)
    assert len(xser) == len(xfser)
    assert len(xfser) == len(ttser)
    length = len(xser)
    out = []

    if is_multiprocess:
        from multiprocessing import Pool, Manager, cpu_count
        mng = Manager()
        pf = mng.dict()
        gpf = mng.dict()
        rpf = mng.dict()
        tdict = mng.dict()
        gtdict = mng.dict()
        rtdict = mng.dict()

        pool = Pool(cpu_count())

        out = pool.map(
            execute,
            [(
                n,x, length,
                pf,gpf,rpf,
                tdict,gtdict,rtdict,
                df, xfser,
                jpstps, enstps,
                nums, plist, endmark,
                tags_b49, tags_b110
            ) for n,x in enumerate(zip(tser,xser,xfser,ttser))])
    else:
        pf = {}
        gpf = {}
        rpf = {}
        tdict = {}
        gtdict = {}
        rtdict = {}

        out = list(map(
            execute,
            [(
                n,x, length,
                pf,gpf,rpf,
                tdict,gtdict,rtdict,
                df, xfser,
                jpstps, enstps,
                nums, plist, endmark,
                tags_b49, tags_b110
            ) for n,x in enumerate(zip(tser,xser,xfser,ttser))]))
        
    out = pd.DataFrame(out)
    out["b1"] = b1(df)

    return out[columns]
    
    
