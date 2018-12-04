import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataVis import df
from sklearn.linear_model import LinearRegression


df_year2017 = df['year'].map(lambda x:x == 2017)
df_uptoOct = df['reference_period_desc'].map(lambda x: x!= 'NOV' and x!= 'DEC')

df_fit = df[df_year2017][df_uptoOct]
#print(df_fit)
#to fit linear regression from Jan-Oct
X = np.array([i for i in range(10)]).reshape(10,1)
#print(X)
y = df_fit["Value"].values
#print(y)

model = LinearRegression()
model.fit(X,y)

#part3a
df_fit.plot(x = 'reference_period_desc',y = 'Value',title = 'Jan-Oct',style='o')
plt.plot(X,model.predict(X))
plt.show()

#predict the value of turkeys as described for November 3(b)
predictedValForNov = model.predict([[10]])
print("The predicted Value for Novemember is: " + str(predictedValForNov))

#absolute error between your predicted value and the actual value of turkeys slaughtered in Virginia in Nov 2017 3(c)
absoluteError = abs(predictedValForNov - 2332000)
print("The absolute error between your predicted value and the actual value of turkeys slaughtered in Virginia in Nov 2017 is: " + str(absoluteError))

#the coefficient of determination, or R^2 value 3(d)
print("R^2 value is: " + str( model.score(X,y)))


# line plot of Values from 2017 along with the linear fit 3(e)
X = np.array([k for k in range(12)]).reshape(12,1)
new_df_2017 = df[df_year2017]
y = new_df_2017["Value"].values
new_df_2017.plot(x = 'reference_period_desc',y = 'Value',title = 'Plot for year 2017',style = 'o')  
model.fit(X,y)
plt.plot(X,model.predict(X))
plt.show()






