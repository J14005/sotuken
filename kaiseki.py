from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *

f = open("AbeShinzo.csv","r",encoding='utf-8')#wadamasamune.csv  AbeShinzo.text
tweet = f.read()
token_filters = [POSKeepFilter('名詞'),TokenCountFilter()]
a = Analyzer(token_filters=token_filters)
for k, v in a.analyze(tweet):
    if(v >=1):
        print("%s: %d" % (k, v))
