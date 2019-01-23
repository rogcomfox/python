import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas
import sklearn

#load the data
oecd_bli = pandas.read_csv("oecd_bli_2015.csv", thousands=',')
gdp_per_capita = pandas.read_csv("gdp_per_capita.csv",thousands=',',delimiter='\t',encoding='latin1', na_values="n/a")

#prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
x = np.c_[country_stats["GDP Per Capita"]]
y = np.c_[country_stats["Life Satisfication"]]

#visualize the data
country_stats.plot(kind='scatter', x="GDP Per Capita",  y='Life Satisfication')
plt.show()

#select a linear model
lin_reg_model = sklearn.linear_model.LinearRegression()

#train the model
lin_reg_model.fit(x, y)

#Make prediction for Cyprus
X_new = [[22857]] #Cyprus GDP Per Capita
print(lin_reg_model.predict(X_new)) #outputs [[5.96242338]]