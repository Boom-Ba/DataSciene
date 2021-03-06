# Simple Linear Regression
## Simple LR on YOE & Salary to find the correlation to predict. 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Train Set- Salary vs Experience & LR fitting line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Test set -Salary vs Experience & LR fitting line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

##Further question to solve
# Make prediction for the salary of an employee who has YOE=12
regressor.predict([[12]]) #predict takes 2d array
##draw the final LR equals by taking look at the coefficient
regressor.coef_
regressor.intercept_
#FINAL LR Formula: Salary= coef_+intercept_