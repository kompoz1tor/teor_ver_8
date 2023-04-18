'''
Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],

ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].

Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy

Полученные значения должны быть равны.

Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.
'''
import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array( [401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
M_X = zp.mean()
M_Y = ks.mean()
M_XY = (zp * ks).mean()
cov_ks = M_XY - M_X * M_Y

np.cov(zp, ks, ddof = 0)
cov_ks2 = ((zp - zp.mean()) * (ks - ks.mean())).mean()
std_X = zp.std()
std_Y = ks.std()
corr_ks = cov_ks / (std_X * std_Y)

print(np.corrcoef(zp, ks))