from datetime import datetime

import numpy as np
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


def get_emotion_peaks(start_date: datetime.date, finish_date: datetime.date, epsilon: float,
                      corpora_name: ExchangeValueName, emotion_type: EmotionType):
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

    X = np.array(emotion_arr)
    date_arr = np.array(date_arr)

    emotion_arr[0] += 1
    start_pos = 0
    i = 1
    zeros = 0
    while i < len(emotion_arr):
        emotion_arr[i] += 1
        if emotion_arr[i] == 1:
            zeros += 1
        elif zeros > 0:
            j = start_pos + 1
            step = abs(emotion_arr[i] - emotion_arr[start_pos]) / (i - start_pos)
            if step == 0:
                step = 0.001
            while j < i:
                if emotion_arr[i] >= emotion_arr[start_pos]:
                    emotion_arr[j] = np.math.ceil(step * (j - start_pos))
                else:
                    emotion_arr[j] = np.math.ceil(step * (i - j - start_pos))
                j += 1
            zeros = 0
            start_pos = i
        else:
            start_pos = i
        i += 1
    emotion_arr = [x if x != 0 else 0.1 for x in emotion_arr]

    pivots = peak_valley_pivots(np.array(emotion_arr).astype(np.double), epsilon,
                                (-1) * epsilon)

    return emotion_arr, date_arr, pivots


def get_next_exchange_peak(date_of_emotion_peak, exchange_date_peak_arr):
    closest_peak_date = max(exchange_date_peak_arr)
    if closest_peak_date < date_of_emotion_peak:
        return None
    for el in exchange_date_peak_arr:
        if el >= date_of_emotion_peak and (el - date_of_emotion_peak) < (closest_peak_date - date_of_emotion_peak):
            closest_peak_date = el
    return closest_peak_date
