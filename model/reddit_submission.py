import datetime
from typing import List

from pony.orm import *

db = Database()
db.bind(provider='mysql', host='localhost', user='root', passwd='password', db='local')


class Submission(db.Entity):
    _table_ = "reddit_submissions"
    id = PrimaryKey(str)
    date_val: datetime.date = Required(datetime.date, column="date")
    title = Required(LongStr)
    url = Required(LongStr)
    score = Required(int)
    text = Optional(LongStr)


db.generate_mapping(create_tables=False)


@db_session
def get_submission(id: str):
    try:
        return Submission[id]
    except ObjectNotFound:
        return None


@db_session
def insert_submission(id: str, date_val: datetime.date, title: str, url: str, score: int, text: str = None):
    try:
        Submission(id=id, date_val=date_val, title=title, url=url, score=score, text=text)
        commit()
    except UnexpectedError:
        pass


@db_session
def get_last_date() -> datetime.date:
    return max(p.date_val for p in Submission)


@db_session
def get_min_date() -> datetime.date:
    return min(p.date_val for p in Submission)


@db_session
def get_submissions_by_date(start_date: datetime.date) -> List[Submission]:
    return Submission.select(lambda p: p.date_val == start_date).prefetch(Submission.text)[:]
