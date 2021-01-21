# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:49:33 2021

@author: Nicolai
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

plt.ion()

data = pd.read_csv('C:/Users/Nicolai/Documents/Bikes_analytics/hour.csv')

# preprocessing

bikes_prep = data.copy()
bikes_prep = bikes_prep.drop(['instant', 'dteday', 'casual', 'registered'], axis=1)


columns = ['season', 'mnth', 'season', 'weekday', 'yr', 'hr', 'workingday', 'weathersit']
names= ['Season', 'Month', 'Season', 'Weekday', 'Year', 'Hour', 'Working day', 'Weather']
dividedBy = ['cnt']
colors = ['g', 'r', 'm', 'b']



plt.subplot(3, 3, 1)
plt.title('Average Demand per season')

cat_list = bikes_prep['season'].unique()
cat_average = bikes_prep.groupby('season').mean()['cnt']

plt.bar(cat_list, cat_average, color=colors)


plt.subplot(3, 3, 2)
plt.title('Average Demand per month')

cat_list = bikes_prep['mnth'].unique()
cat_average = bikes_prep.groupby('mnth').mean()['cnt']

plt.bar(cat_list, cat_average, color=colors)

plt.subplot(3, 3, 3)
plt.title('Average Demand per holiday')

cat_list = bikes_prep['season'].unique()
cat_average = bikes_prep.groupby('season').mean()['cnt']

plt.bar(cat_list, cat_average, color=colors)



plt.subplot(3, 3, 4)
plt.title('Average Demand per Weeks day')

cat_list = bikes_prep['weekday'].unique()
cat_average = bikes_prep.groupby('weekday').mean()['cnt']

plt.bar(cat_list, cat_average, color=colors)


plt.subplot(3, 3, 5)
plt.title('Average Demand per year')

cat_list = bikes_prep['yr'].unique()
cat_average = bikes_prep.groupby('yr').mean()['cnt']

plt.bar(cat_list, cat_average, color=colors)


plt.subplot(3, 3, 6)
plt.title('Average Demand per Hour')

cat_list = bikes_prep['hr'].unique()
cat_average = bikes_prep.groupby('hr').mean()['cnt']

plt.bar(cat_list, cat_average, color=colors)


plt.subplot(3, 3, 7)
plt.title('Average Demand per Working day')

cat_list = bikes_prep['workingday'].unique()
cat_average = bikes_prep.groupby('workingday').mean()['cnt']

plt.bar(cat_list, cat_average, color=colors)


plt.subplot(3, 3, 8)
plt.title('Average Demand per Weather')

cat_list = bikes_prep['weathersit'].unique()
cat_average = bikes_prep.groupby('weathersit').mean()['cnt']


plt.bar(cat_list, cat_average, color=['g', 'r', 'm', 'b'])

plt.tight_layout()

plt.show()



