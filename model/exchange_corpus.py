from typing import List

from pony.orm import *

from model.exchange_value_name import ExchangeValueName

db = Database()
db.bind(provider='mysql', host='localhost', user='root', passwd='password', db='local')


class ExchangeCorpus(db.Entity):
    _table_ = "exchange_corpora"
    id = PrimaryKey(int, auto=True)
    corpus_name = Required(str)
    word = Required(str)


db.generate_mapping(create_tables=False)


@db_session
def get_words_of_corpus(corpus: ExchangeValueName) -> List[str]:
    return select(p.word for p in ExchangeCorpus if p.corpus_name == corpus.value).prefetch(ExchangeCorpus.word)[:]
