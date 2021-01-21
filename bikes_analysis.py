# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:44:08 2021

@author: Nicolai
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math




data = pd.read_csv('hour.csv')

# preprocessing

bikes_prep = data.copy()
bikes_prep = bikes_prep.drop(['instant', 'dteday', 'casual', 'registered'], axis=1)

colors = ['g', 'r', 'm', 'b']



print(bikes_prep.columns.values[:-5])



for i in range(len(bikes_prep.columns.values[:-5]) - 1):
    columns = ['Season', 'Year', 'Month', 'Hour', 'Holiday', 'Weekday', 'Working day', 'Weather']
    fig = plt.figure(figsize=(3, 2))
    ax = fig.add_axes([0,0,1,1])
    
    ax.set_title(f'Average Demand per {columns[i]}')
    
    
    ax.set_ylabel('Demand', fontsize = 12)
    ax.set_xlabel(columns[i], fontsize = 12)
    
    cat_list = bikes_prep[bikes_prep.columns.values[i]].unique()
    cat_average = bikes_prep.groupby(bikes_prep.columns.values[i]).mean()['cnt']
    
    ax.bar(cat_list, cat_average, color=colors)
    
    
    plt.savefig(f'C:/Users/Nicolai/Documents/Bikes_analytics/{bikes_prep.columns.values[i]}.png', dpi=200, format='png', bbox_inches='tight')
    
    plt.show()










