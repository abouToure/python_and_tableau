# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 23:10:13 2024

@author: aboub
"""

import pandas as pd

data = pd.read_csv('transaction.csv',sep=';')

#CostPerTransaction calcul

CostperItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostperItem * NumberOfItemsPurchased

#Adding a new colum to a dataFrame
data['CostPerTransaction'] = CostPerTransaction
    
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales - cost)/cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']
data['Markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']


#Round marking

data['Markup'] = round(data['Markup'], 2)

#Checking column dtype

print(data['Day'].dtype)

#change column type

day = data['Day'].astype(str)
year = data['Year'].astype(str)

my_date = day+'-'+data['Month']+'-'+year

data['Date'] = my_date

data.iloc[0] # View de row with index 0
data.iloc[0:3] # first 3 row
data.iloc[:,2] # bring all row, 2nd column 
data.iloc[4,2] # bring in 4th rows 2nd colum 


#new-var = column.str.split(',',extend=True)

Split_col = data['ClientKeywords'].str.split(',', expand = True)

#Creating new column for the split column in client keywords

data['ClientAge'] = Split_col[0] 
data['ClientType'] = Split_col[1]
data['LengthOfContract'] = Split_col[2]


#using the replace function 

data['ClientAge'] = data['ClientAge'].str.replace('[','') 
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#using the lower function to change item to lowercas

data['ItemDescription'] = data['ItemDescription'].str.lower()

# how to merge file

# bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';') 

#mergin files: merge_df = pd.merge(df_old,df_new, on='key')

data = pd.merge(data, seasons, on = 'Month')

# Dropping columns 

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year','Month'], axis = 1)

#export into csv

data.to_csv('valueInc_cleaned.csv', index = False)

