from datetime import datetime
from typing import List

import numpy as np
import peakutils as peakutils
from zigzag.core import peak_valley_pivots

from model.emotion_type import EmotionType
from model.exchange_value import get_exchange_values_between
from model.exchange_value_name import ExchangeValueName
from tools.analyzed_submissions import get_emotions_between


def get_exchange_peaks(start_date: datetime.date, finish_date: datetime.date, epsilon: float,
                       exchange_value_name: ExchangeValueName):
    ex_arr = get_exchange_values_between(start_date, finish_date)
    exchange_arr = [getattr(ex_el, exchange_value_name.value) for ex_el in ex_arr]
    date_arr = [p.date_val for p in ex_arr]

    exchange_arr = np.array(exchange_arr)
    date_arr = np.array(date_arr)
    pivots = peak_valley_pivots(exchange_arr, epsilon, (-1) * epsilon)

    return exchange_arr, date_arr, pivots


def get_emotions(start_date: datetime.date, finish_date: datetime.date, corpora_name: ExchangeValueName,
                 emotion_type: EmotionType, epsilon: int):
    em_arr = get_emotions_between(start_date, finish_date)
    emotion_arr = []
    date_arr = []
    for post in em_arr:
        date_arr.append(post['date'].date())
        corpora = post['corpora']
        for el in corpora:
            if el['name'] == corpora_name.value:
                if emotion_type == EmotionType.POSITIVE:
                    emotion_arr.append(el['positive_mentions'])
                else:
                    emotion_arr.append(el['negative_mentions'])

    peaks = peakutils.indexes(np.array([x if x >= epsilon else 0 for x in emotion_arr]))
    pivots = np.array([1 if x in peaks else 0 for x in [i for i in range(len(emotion_arr))]])
    emotion_arr = np.array(emotion_arr)

    date_arr = np.array(date_arr)

    return emotion_arr, date_arr, pivots


def get_next_exchange_peak(date_of_emotion_peak, exchange_date_peak_arr):
    closest_peak_date = max(exchange_date_peak_arr)
    if closest_peak_date < date_of_emotion_peak:
        return None
    for el in exchange_date_peak_arr:
        if el >= date_of_emotion_peak and (el - date_of_emotion_peak) < (closest_peak_date - date_of_emotion_peak):
            closest_peak_date = el
    return closest_peak_date


def get_bears_and_bulls(exchange_date_arr: List[datetime.date], exchange_pivots,
                        emotion_peak_date_arr: List[datetime.date]):
    exchange_peak_date_arr = exchange_date_arr[exchange_pivots == 1]
    exchange_valley_date_arr = exchange_date_arr[exchange_pivots == -1]

    bears_after = 0
    bulls_after = 0
    for el in emotion_peak_date_arr:
        closest_peak = get_next_exchange_peak(el, exchange_peak_date_arr)
        closest_valley = get_next_exchange_peak(el, exchange_valley_date_arr)
        if closest_peak is not None and closest_valley is not None:
            if (closest_peak - el) < (closest_valley - el):
                bears_after += 1
            else:
                bulls_after += 1
        if closest_peak is not None and closest_valley is None:
            bears_after += 1
        if closest_valley is not None and closest_peak is None:
            bulls_after += 1

    return bears_after, bulls_after
