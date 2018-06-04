from datetime import date, timedelta
from datetime import datetime
from statistics import pvariance, mean

from pymongo import MongoClient
from textblob import TextBlob

from config.corpora import *
from model.exchange_value_name import ExchangeValueName
from model.reddit_submission import get_min_date, get_submissions_by_date

all_corpora = {ExchangeValueName.USD.value: DOLLAR_CORPUS, ExchangeValueName.JPY.value: YEN_CORPUS,
               ExchangeValueName.GBP.value: POUND_CORPUS, ExchangeValueName.EUR.value: EURO_CORPUS}

client = MongoClient('localhost', 27017)
db = client['reddit']
# db['common_submissions'].drop()
collection = db['common_submissions']

if __name__ == '__main__':

    start_date: date = get_min_date()
    finish_date: date = start_date + timedelta(days=1)

    while finish_date <= datetime.now().date():
        if collection.find_one({"date": datetime.combine(start_date, datetime.min.time())}) is not None:
            continue
        submissions = get_submissions_by_date(start_date)

        date_entity = {}
        corpora = []
        for key, value in all_corpora.items():
            corpus_entity = {}
            words = []
            for word in value:
                word_entity = {}
                weights = []
                for submission in submissions:
                    blob = TextBlob(submission.text)
                    for sentence in blob.sentences:
                        if word in sentence:
                            weights.append(sentence.sentiment.polarity)
                word_entity['name'] = word
                word_entity['weights'] = weights
                word_entity['M'] = len(weights)
                if len(weights) > 2:
                    word_entity['average'] = mean(weights)
                    word_entity['dispersion'] = pvariance(weights, word_entity['average'])
                words.append(word_entity)

            corpus_entity['name'] = key
            corpus_entity['words'] = words
            corpora.append(corpus_entity)

        date_entity['corpora'] = corpora
        date_entity['date'] = datetime.combine(start_date, datetime.min.time())

        collection.insert_one(date_entity)
        start_date = finish_date
        finish_date = start_date + timedelta(days=1)
