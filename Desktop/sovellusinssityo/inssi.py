import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression 
import statsmodels.api as sm
from statsmodels.formula.api import ols
import mysql.connector
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
import pyodbc

# Data preparation
X = df['. . .'].to_frame()
# Preparation of variables
y = df['. . .'] 

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:10:55 2020
@author: Evgeni
"""

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password=" ",
 database="statistic_x"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM gin"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
 print(x)

SQL_Query = pd.read_sql_query(sql, mydb)
df = pd.DataFrame(SQL_Query,columns=['vuosi', 'rahatulot', 'tuotannontulot', 'bruttotulot'])
print("Data of DataFrame from MySQL database")
print(df) 

# -*- coding: utf-8 -*-
18
"""
Created on Fri Oct 8 22:06:25 2021
@author: Hei
"""

# MySQL database
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password=" ",
 database="statistic_x"
)
# Use mycursor method
mycursor = mydb.cursor()
sql = "SELECT * FROM gin"
mycursor.execute(sql)
myresult = mycursor.fetchall()
19
# Get DataFrame
SQL_Query = pd.read_sql_query(sql, mydb)
df = pd.DataFrame(SQL_Query,columns=['vuosi', 'rahatulot', 'tuotannontulot', 'bruttotulot'])
print("Data of DataFrame from MySQL database")
print(df)
# Visualization of variables
plt.xlabel('tuotannontulot')
plt.ylabel('bruttotulot')
plt.scatter(df.tuotannontulot,df.bruttotulot, color = 'dark red',
marker= '*')
# Linear regression function
reg = linear_model.LinearRegression()
reg.fit(df[['tuotannontulot']],df.bruttotulot)
# Get linear regression results
plt.scatter(df.tuotannontulot,df.bruttotulot, color = 'dark red',
marker= '*')
plt.plot(df.tuotannontulot,reg.predict(df[['tuotannontulot']]),color =
'black')
predicted_bruttotulot = reg.predict(df[['tuotannontulot']])
gradient = reg.coef_ # gradient or slope
intercept = reg.intercept_ # it is intercept
r2 = r2_score(df.bruttotulot,predicted_bruttotulot)
mse = mean_squared_error(df.bruttotulot,predicted_bruttotulot)
plt.show()
print("Linear regression: ")
print("The r-square value is :", r2)
print("Mean square error is :",mse)
print("The gradient is : ",gradient)
print("The intercept is :",intercept)

SQL_Query = pd.read_sql_query(sql, mydb)
df = pd.DataFrame(SQL_Query,columns=['vuosi', 'rahatulot', 'tuotannontulot', 'bruttotulot'])
print("Data of DataFrame from MySQL database")
print(df)
# Variables and DataFrame
X = df[['bruttotulot']]
y = df['rahatulot']
# Cross-validation
cv = KFold(n_splits=33, random_state=1, shuffle=True)
# Linear regression model
model = LinearRegression()
# Get k-fold
scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error',
 cv=cv, n_jobs=-1)
# We can get mean absolute error
mean(absolute(scores))
print("Cross-Validation: ",mean(absolute(scores))) 

X = df[['tuotannontulot']]
y = df['bruttotulot']
# We can get cross-validation
cv = KFold(n_splits=33, random_state=1, shuffle=True)
# We can get linear regression model
model = LinearRegression()
# It is k-fold
scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error',
 cv=cv, n_jobs=-1)
# This is mean absolute error
mean(absolute(scores))
print("Cross-Validation: ",mean(absolute(scores))) 

# Function of linear regression
reg = linear_model.LinearRegression()
reg.fit(df[['bruttotulot']],df.rahatulot)
# Linear regression results
plt.scatter(df.bruttotulot,df.rahatulot, color = 'dark red', marker=
'*')
plt.plot(df.bruttotulot,reg.predict(df[['bruttotulot']]),color =
'black')
predicted_rahatulot = reg.predict(df[['bruttotulot']])
# Gradient or slope
gradient = reg.coef_
# It is intercept
intercept = reg.intercept_
r2 = r2_score(df.rahatulot,predicted_rahatulot)
mse = mean_squared_error(df.rahatulot,predicted_rahatulot)
plt.show()

# Linear regression model
model = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=1/3, random_state=0)
model.fit(X_train, y_train)
# Visualization of the training program
visual_train = plt
visual_train.scatter(X_train, y_train, color='red')
visual_train.plot(X_train, model.predict(X_train), color='blue')
visual_train.title('Bruttotulot-tuotannontulot (Training set)')
visual_train.xlabel('tuotannontulot')
visual_train.ylabel('bruttotulot')
visual_train.show()
# Visualization of the test program
visual_test = plt
visual_test.scatter(X_test, y_test, color='red')
visual_test.plot(X_train, model.predict(X_train), color='blue')
visual_test.title('Bruttotulot-tuotannontulot (Test set)')
visual_test.xlabel('tuotannontulot')
visual_test.ylabel('bruttotulot')
visual_test.show() 

# Linear regression results
plt.scatter(df.bruttotulot,df.rahatulot, color = 'dark red', marker=
'*')
plt.plot(df.bruttotulot,reg.predict(df[['bruttotulot']]),color =
'black')
predicted_rahatulot = reg.predict(df[['bruttotulot']])
# Gradient or slope
gradient = reg.coef_
# It is intercept
intercept = reg.intercept_
r2 = r2_score(df.rahatulot,predicted_rahatulot)
mse = mean_squared_error(df.rahatulot,predicted_rahatulot)
plt.show()

model = ols('rahatulot ~ bruttotulot', data=df).fit()
# Get model summary
print(model.summary())
# Define figure size
fig = plt.figure(figsize=(12,8))
# Produce residual plots
fig = sm.graphics.plot_regress_exog(model, 'bruttotulot', fig=fig) 


