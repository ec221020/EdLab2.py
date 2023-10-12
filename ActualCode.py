import unittest 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def dataframe_to_dictionary(df):
    dictionary = {}
    for header in df:
        dictionary[header] = [data for data in df[header]]
    return dictionary

todaysData = pd.read_csv("C:\\\\Users\\ec221020\\Downloads\\DATAFORTODAY.csv")
datadataForToday = dataframe_to_dictionary(todaysData)

df = pd.read_csv("C:\\\\Users\\ec221020\\Downloads\\DATAFORTODAY.csv")
df.head()
print(df)

x = dataframe_to_dictionary(df)
xCoords = x["X"]
yCoords = x["Y"]
xCoords = np.array(xCoords)
yCoords = np.array(yCoords)
print(type(xCoords[0]))

import numpy as np
x = xCoords
y = yCoords

def linear_regression(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)
    sigmax = np.std(x)
    sigmay = np.std(y)
    sigmaxy = np.sum(np.multiply(x-meanx,y-meany))/(len(x)-1)
    m = sigmaxy/(sigmax*sigmax)
    q = meany-m*meanx
    print(m, q)
    return m,q

lin_reg_m_main, lin_reg_q_main = linear_regression(x, y)
y_main = lin_reg_m_main * xCoords + lin_reg_q_main
plt.figure()

plt.plot(xCoords, yCoords, 'o')
plt.xlabel("88")
plt.ylabel("DST")
plt.title("NGJ")
plt.plot(xCoords, y_main, label="NBHV")
plt.legend()
# Display
plt.show()