# domextract
Web content extractor for articles.

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

```python3
import requests
import domextract
from bs4 import BeautifulSoup

ext = domextract.Extractor()

def clean(html):
    soup = BeautifulSoup(html, "html.parser")
    [x.extract() for x in soup.find_all('script')]
    [x.extract() for x in soup.find_all('style')]
    [x.extract() for x in soup.find_all('meta')]
    [x.extract() for x in soup.find_all('noscript')]
    return str(soup)

def extract(url):
    r = requests.get(url)
    data = r.content
    result = ext.extract(clean(data), is_url=str)
    return result
    
print(extract("https://www.indiatoday.in/cities/mumbai/story/mumbai-local-train-fully-vaccinated-covid-bmc-ease-cubs-1827826-2021-07-14"))
```

[output]

```
BMC could ease curbs in local trains in 2nd phase for those fully vaccinated The Brihanmumbai Municipal Corporation is mulling on easing curbs for those fully vaccinated against Covid-19 in local trains in the second phase of unlocking. Local trains are one of the major means of transportation in Mumbai. The Brihanmumbai Municipal Corporation is mulling on easing curbs in local trains for those fully vaccinated against Covid-19 in the second phase of the unlocking. The final decision on this will, however, be taken by the Maharashtra government. This comes after the civic body wrote to the state government, requesting that fully vaccinated passengers be exempted from carrying an RT-PCR negative test report to the airport. Speaking to India Today TV, BMC chief Iqbal Singh Chahal expressed confidence at the present Covid-19 situation in Mumbai. He said the situation is under control at the moment. “Looking at the current Covid-19 chart we can easily say that we are in a very comfortable position at the present moment. Our doubling rate is nearly at a thousand days now," he said. Read:  Maharashtra: Districts with high positivity rate not contact tracing enough, say experts "And we are getting just 400-500 cases and that is also because we are doing nearly 40,000 tests daily. The death count is also very low in the city. It’s difficult to make the count zero for a city like Mumbai, but the current situation is stable in our assessment.” he said. On the question of ordering relaxations for the fully vaccinated citizens in the locals, the BMC chief said the decision would be taken in the second phase. “In local trains, we are mostly doing Rapid Antigen tests. There is surveillance and random tests at the present moment. It’s not possible to have an RT-PCR test for lakhs for passengers. But this too would be taken up in the second phase.” he said. Talking to India Today TV, Dr. Lancelot Pinto, Consultant Pulmonologist, PD Hinduja Hospital & MRC said, "A negative RT-PCR done within 48 hours of travel does not necessarily mean that the person isn’t infected, especially if the person has no symptoms. It does, however, make travel difficult, especially for those making day trips on business, for whom, landing, getting RT-PCR results, and coming back on the same day is logistically not feasible. I think the combination of these two reasons drove this decision. They are, however, waiving off the requirement only for those who are fully vaccinated, adding a layer of safety, as such individuals are less likely to be infected." "The same rationale could be applicable to train travelers as well. In both cases (air travel and train travel), temperature checks, strict masking enforcement would add to the layers of safety. No method is going to be foolproof, we need to add as many layers of safety as feasible while trying to get the economy and back to normal," he said. Here’s a look at the latest Covid-19 graph in Mumbai :  - 441 new cases and 8 deaths - Active cases - 6950 - Recovery Rate - 96% - Doubling Rate -925 days - Active containment zones -5 - Active sealed buildings -65 - ICU beds - 2352 - Ventilator beds - 1294 - Oxygen beds - 9112 Click here for IndiaToday.in’s  complete coverage of the coronavirus pandemic.
```
