__author__ = 'Ben'

import numpy as np
import pandas as pd
import statsmodels.api as sm
import pylab as pl


df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")

print(df.head())
print()
print()

df.columns = ["admit", "gre", "gpa", "prestige"]

dummy_ranks = pd.get_dummies(df['prestige'], prefix='prestige')

cols_to_keep = ['admit', 'gre', 'gpa']

data = df[cols_to_keep].join(dummy_ranks.ix[:, 'prestige_2':])

data['intercept'] = 1.0

train_cols = data.columns[1:]

logit = sm.Logit(data['admit'], data[train_cols])

result = logit.fit()

print(result.summary())
print()
print()

print(np.exp(result.params))


