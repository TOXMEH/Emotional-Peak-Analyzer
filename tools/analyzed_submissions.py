from datetime import datetime

import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['reddit']
collection = db['common_submissions']
# db['analyzed_submissions'].drop()
result_collection = db['analyzed_submissions']
EPSILON = 0.1

if __name__ == '__main__':
    for stat in collection.find():
        # if result_collection.find_one({"date": stat['date']}) is not None:
        #     continue
        result = {'date': stat['date']}
        corpora = []
        for corpus in stat['corpora']:
            corpus_entity = {'name': corpus['name']}
            words = []
            corpus_positive_mentions = 0
            corpus_negative_mentions = 0
            for word in corpus['words']:
                word_entity = {'name': word['name']}
                word_positive_mentions = 0
                word_negative_mentions = 0
                for weight in word['weights']:
                    if weight > EPSILON:
                        word_positive_mentions += 1
                    elif weight < (-1) * EPSILON:
                        word_negative_mentions += 1
                word_entity['positive_mentions'] = word_positive_mentions
                word_entity['negative_mentions'] = word_negative_mentions
                corpus_positive_mentions += word_positive_mentions
                corpus_negative_mentions += word_negative_mentions
                words.append(word_entity)

            corpus_entity['words'] = words
            corpus_entity['positive_mentions'] = corpus_positive_mentions
            corpus_entity['negative_mentions'] = corpus_negative_mentions
            corpora.append(corpus_entity)

        result['corpora'] = corpora
        result_collection.insert_one(result)


def get_emotions_between(start_date: datetime.date, finish_date: datetime.date):
    return result_collection.find({"date": {'$gte': datetime.combine(start_date, datetime.min.time()),
                                            '$lt': datetime.combine(finish_date, datetime.min.time())}}).sort('date',
                                                                                                              pymongo.ASCENDING)
