import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('../../ML/data-resource_2016_10_24_gdp-growth-rate-in-bangladesh.csv')

print(data)
print(data.describe())

y = data['Year']
x1 = data['GDP Growth Rate']

x=sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results_summary = results.summary()
print(results_summary)

plt.scatter(x1,y)
plt.xlabel('GDP Growth Rate', fontsize=15)
plt.ylabel('Year', fontsize=15)
plt.show()

plt.scatter(x1,y)
yhat = 5.8385*x1 + 1977.052
fig = plt.plot(x1,yhat, lw=4, c='orange', label = 'regression line')
plt.xlabel('GDP Growth Rate', fontsize = 15)
plt.ylabel('Year', fontsize = 15)
plt.show()