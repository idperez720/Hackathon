# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 02:10:56 2021

@author: pc
"""

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

lin_reg = LinearRegression()
lin_reg.fit(Entrenamiento,labels)

#Predecir
predictionsLin = lin_reg.predict(datosParaProbar)

forest = RandomForestRegressor()
forest.fit(Entrenamiento,labels)

predictionsForest = forest.predict(datosParaProbar)

