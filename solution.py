import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 287133833 # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = 1 / np.sqrt(len(x))
    return 2/25*(loc + 0.5 - scale * norm.ppf(1 - alpha / 2)), \
           2/25*(loc + 0.5 - scale * norm.ppf(alpha / 2))
