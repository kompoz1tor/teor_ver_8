'''
Измерены значения IQ выборки студентов,

обучающихся в местных технических вузах:

131, 125, 115, 122, 131, 115, 107, 99, 125, 111.

Известно, что в генеральной совокупности IQ распределен нормально.

Найдите доверительный интервал для математического ожидания с надежностью 0.95.
'''
import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
x_mean = x.mean()
x_std = x.std(ddof = 1)
x_mean_std = x_std / (np.sqrt(len(x)))
result = t_stat(x_mean, x_mean_std, len(x) - 1, 0.05, 'two-sided')
print(f'Доверительный интервал для математического ожидания с надежностью 0.95: {result}')
