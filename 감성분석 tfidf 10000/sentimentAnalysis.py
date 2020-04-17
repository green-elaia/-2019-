from konlpy.tag import Okt
import json
import numpy as np
from tensorflow.keras import models

okt = Okt()

with open('selected_words.json', encoding = 'UTF-8') as f:
        selected_words = json.load(f)

model = models.load_model('second_model.h5')

def tokenize(doc):
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

def predict_sentiment(review):
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = float(model.predict(data))
    if(score > 0.5):
        return 1
    else:
        return 0
