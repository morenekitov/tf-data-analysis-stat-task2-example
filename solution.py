import pandas as pd
import numpy as np

from scipy.stats import laplace


chat_id = 287133833 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x =  2 * x / (88 * 88)
    alpha = 1 - p
    loc = x.mean()
    
    
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * laplace.ppf(1 - alpha / 2), \
           loc - scale * laplace.ppf(alpha / 2)
