# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 06:13:26 2020

@author: NANI
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.metrics import mean_squared_error,r2_score
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x=pd.read_csv('https://raw.githubusercontent.com/rmadan16/LinearRegression_CarPrice/master/CarPrice_Assignment.csv')
y=x.price  #target variable
#Whether to drop labels from the index (0 / ‘index’) or columns (1 / ‘columns’).
x=x.drop(['price'],axis=1)
#print(x.head(5))

#Checking for null values or Datapreprocessing
#print('no.of null values in x =',x.isnull().sum())
#print('no.of null values in y =',y.isnull().sum())

#Understanding the dataset
#print(x.shape)
#print(y.shape)
#print('Describing dataframe ',x.describe(include='all'))

#Understanding relationship between dataset using visualization
#1. The above 3 lines displays a 15X15 graph plots of all numeric columns
#plt.rcParams['figure.figsize']=[16,9]
#sns.set(style='darkgrid')
#sns.pairplot(data=x)

#2. The above 3 lines displays a 15X15 graph plots of all numeric columns
#scatter_matrix(x,alpha=0.5,figsize=(30,30),diagonal='kde',grid=True)
#sns.set(rc={'figure.figsize':(11.7,8.27)})
#sns.distplot(y,bins=30)
# distplot combines the matplotlib hist function (with automatic calculation of a good default bin size) with the seaborn kdeplot() and rugplot() functions
#i.e instead of hist in diag place we will get kde and rug
#plt.show()

#3. The above 3 lines displays a 15X15 graph plots of all numeric columns
#Plot Y in timeseries data
#Plot Y in timeseries data
#y.plot()

#displot - Heat map and correlation matrix
#correlation_matrix=x.corr().round(2)
#print(correlation_matrix)
#sns.heatmap(data=correlation_matrix,annot = True)

#Copying all categorical data into another dataframe using copy
cat = x.select_dtypes(include=['object']).copy(deep='False')
#When deep=False, a new object will be created without copying the calling object’s data or index
#Any changes to the data of the original will be reflected in the shallow copy (and vice versa).
cat=cat.iloc[:,:].apply(pd.Series) #can add index values, automatically excludes missing data
name = cat.CarName.copy()
#print(name.head())
#Splitting all the values of CarName
temp=[]
temp=name.str.split(pat=' ',expand = True) #expand is used to expand the lsit to diff columns
#print(temp.head())
temp=temp[0]
#print(temp.head())

#to find any spelling mistakes count the occurences of cars if the number is 1 or 2 there can be an error
print(cat.CarName.value_counts())

#Replacing bad spellings with right spellings
cleanup_nums = {'CarName': { 'maxda': 'mazda' , 'porcshce': 'porsche' , 'Nissan':'nissan' , 'vokswagen':'volkswagen', 'toyouta' : 'toyota','vw' : 'volkswagen'} }
x.replace(cleanup_nums,inplace=True)

#encoding i.e changing catagorical to int
#print(X[‘doornumber’].value_counts())
cleanup_nums = {'doornumber': {'four': 4, 'two': 2},
 'cylindernumber': {'four': 4, 'six': 6, 'five': 5, 'eight': 8,
 'two': 2, 'twelve': 12, 'three':3 }}
x.replace(cleanup_nums, inplace=True)
#print(x['cylindernumber'].head())

#OneHotEncoding using dummy method
m=x.copy(deep='False')
m=pd.get_dummies(m,columns=cat.columns)
print(x.columns)
print(m.columns)












