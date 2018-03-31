#coding=utf-8

from sklearn.linear_model import LinearRegression, Lasso
from scipy.optimize import minimize, linprog
import numpy as np


class Optimizer:
    def __init__(self):
        pass

    def optimize(self, origin_budget):
        default_target = self.model.predict([origin_budget])[0]

        random_gen = np.random.RandomState(42)

        best_budget = origin_budget

        # Ограничения
        xmin_bounds = [i*0.95 for i in origin_budget]
        xmax_bounds = [i*1.05 for i in origin_budget]
        bounds = list(zip(xmin_bounds, xmax_bounds))

        # Веса текущей модели
        # weights = self.model.coef_
        weights = (0.05 + random_gen.exponential(0.75, size=15)) * 2

        origin = np.zeros(2)
        origin[0] = np.dot(origin_budget, weights)
        origin[1] = np.dot(origin_budget, weights)

        weights_tmp = np.zeros((2,15))
        weights_tmp[0,:] = weights
        weights_tmp[1,:] = weights

        # Оптимизация
        opt = linprog(origin_budget, -weights_tmp, -origin, bounds = bounds)
        optimized_budget = np.array(opt.x)

        return optimized_budget

    def fit(self, X_data, y_data):
        self.model = LinearRegression().fit(X_data, y_data)
