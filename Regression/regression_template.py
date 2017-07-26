## Regression Template ##

# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Import the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Encode categorical data
"""from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoid Dummy Variable Trap
X = X[:, 1:]"""


# Split dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""


# Fit Regression Model (Create regressor)

# Sample multiple linear regression
"""from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)"""

# Sample ploynomial regression
"""from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly_fetr = PolynomialFeatures(degree=3)
X_poly = poly_fetr.fit_transform(X)
regressor = LinearRegression()
regressor.fit(X_poly, y)"""


# Predict result
y_pred = regressor.predict(420)

# Visualize result
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('ML Study (Regression Model)')
plt.xlabel('X Lable')
plt.ylabel('Y Lable')
plt.show()

# Visualize result in higher resolution with smoother curve
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('ML Study (Regression Model)')
plt.xlabel('X Lable')
plt.ylabel('Y Lable')
plt.show()
