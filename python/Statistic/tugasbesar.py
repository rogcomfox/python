import pandas as pd
from sklearn import linear_model, metrics
import matplotlib.pyplot as plt

#Read Data
data = pd.read_csv("E:/dataskuy.csv")
df = pd.DataFrame(data)

#Plot Data to matplotlib
plt.scatter(df['T'], df['BI'], color='red')
plt.title('T vs BI', fontsize=14)
plt.xlabel('T', fontsize=14)
plt.ylabel('BI', fontsize=14)
plt.grid(True)
plt.show()

#Train Data
x = df.iloc[:, 5].values
y = df.iloc[:, 7].values
#Reshape Data
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
#Linear Regression
regr = linear_model.LinearRegression()
s = regr.fit(x, y)
data_pred = regr.predict(x)

#print coefficient
print('Coefficients: \n', regr.coef_)
print('R Square: %.3f'
    % metrics.r2_score(y, data_pred))    
print("Mean squared error: %.5f" 
    % metrics.mean_squared_error(y, data_pred))
# Explained variance score: 1 is perfect prediction
print('Explained Variance score: %.5f' 
    % metrics.explained_variance_score(y, data_pred))

# Plot outputs
plt.scatter(x, y,  color='black')
plt.plot(x, data_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()