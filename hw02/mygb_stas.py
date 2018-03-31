#coding=utf-8

from sklearn.base import BaseEstimator
from sklearn.tree import DecisionTreeRegressor
import numpy as np


# Параметрами с которыми вы хотите обучать деревья
TREE_PARAMS_DICT = {'max_depth': 7}
# Параметр tau (learning_rate) для вашего GB
TAU = 0.015


class SimpleGB(BaseEstimator):
    def __init__(self, tree_params_dict, iters, tau):
        self.tree_params_dict = tree_params_dict
        self.iters = iters
        self.tau = tau
        
    def fit(self, X_data, y_data):
        self.base_algo = DecisionTreeRegressor(**self.tree_params_dict).fit(X_data, y_data)
        self.estimators = []
        curr_pred = self.base_algo.predict(X_data)
        for iter_num in range(self.iters):
            # Нужно посчитать градиент функции потерь
            grad = []
            for i,j in zip(y_data, curr_pred):
                if i == 1:
                    grad.append( self.tau / j )
                else:
                    grad.append( -self.tau /(1 - j) )
            #grad = 2*(y_data - curr_pred)* self.tau
            # Нужно обучить DecisionTreeRegressor предсказывать антиградиент
            # Не забудьте про self.tree_params_dict
            algo = DecisionTreeRegressor(**self.tree_params_dict).fit(X_data, grad) # TODO
            self.estimators.append(algo)
            # Обновите предсказания в каждой точке
            curr_pred += algo.predict(X_data)
        return self
    
    
    def predict(self, X_data):
        # Предсказание на данных
        res = self.base_algo.predict(X_data)
        for estimator in self.estimators:
            res += self.tau * estimator.predict(X_data)
        # Задача классификации, поэтому надо отдавать 0 и 1
        return list(map(lambda x: 1 if x > 0.5 else 0, res))
