__author__ = 'Ben'

import pandas as pd
from lifelines import CoxPHFitter
from lifelines.utils import k_fold_cross_validation
from matplotlib import pyplot as plt
from lifelines import KaplanMeierFitter

def make_plot():

    # Tests to make sure the data will be converted to a dataframe correctly
    # This data frame is also used in the various tests
    #
    # Test successful on 11/20/2014 3:11 am with top 20 proteins as data set
    data = pd.read_csv('Scripts/compiled_data.csv', header=0)

    #print(data.head())





    # Test of k fold cross validation based on cox proportional hazard model
    # k initially set to 5
    #
    # 1.0 = perfect concordance
    # 0.0 = perfect anit-concordance
    # 0.5 = result from random
    #
    # Test failure: delta contains nan values. 3:13am
    # Changing missing values (originally -1) to 0 had no noticeable affect
    # Meth values might be too small for a significant variance to be found.
    # Multiplying all meth values by 100 had no noticeable affects
    # No solution found as of 4:00 am, moving on.

    # cf = CoxPHFitter()
    #
    # scores = k_fold_cross_validation(cf, data, duration_col='day', event_col='status', k=5)
    #
    # print(scores)
    # print(scores.mean())
    # print(scores.std())





    # Test of Cox's hazard model.  Should give some idea of which variants are most important.
    #
    # Important mutations (not currently reliable): EIF2AK2, SUV39H1, SHC1, ZNF238
    # Important meth values: FLT3LG
    # Important rpkm values: RARB
    #
    # Test successful with modified top 20 proteins. 4:15am

    cf = CoxPHFitter(alpha=.95, tie_method='Efron')
    cf.fit(data, duration_col='day', event_col='status')

    # print(cf.summary())

    # Test on KM fitting and plotting

    ax = plt.subplot(111)

    T = data['day']
    E = data['status']

    kmf = KaplanMeierFitter()
    kmf.fit(T, event_observed=E)

    kmf.plot(ax=ax)

    plt.savefig('pamlla/templates/foo.png')