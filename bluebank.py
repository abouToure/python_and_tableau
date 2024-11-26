# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:25:06 2024

@author: aboub
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file) 

#transform to dataFrame
loandata = pd.DataFrame(data)

#findind unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()


#describe the data for the specific column
loandata['int.rate'].describe()
loandata['dti'].describe()

#using EXP to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#applying for loop for loand data
lenght = len(loandata)

ficocat = []
for i in range(0,lenght):
    category = loandata['fico'][i]
    if category >=300 and category <400:
        cat = 'Very Poor'
    elif category >=400 and category <600:
        cat = 'Poor'
    elif category >=601 and category <660:
        cat = 'Fair'
    elif category >=660 and category <700:
        cat = 'Good'
    elif category >=700 :
        cat = 'Excellent'
    else:
        cat = "Unknow"
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.loc as a conditional statement 
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loan/row by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green', width=0.1)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

loandata.to_csv('loan_cleaned.csv', index=True)










