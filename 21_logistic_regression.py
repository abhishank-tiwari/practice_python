import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
cwd=os.getcwd()
#print(cwd)           
dataset = pd.read_csv(".\csv\exms.csv") #RELATIVE_PATH
plt.scatter(dataset ['age'], dataset ['loan'])
plt.show()
x_train , x_test , y_train , y_test = train_test_split (dataset ["age"], dataset ["loan"],train_size = 0.8 , random_state = 10)
model = LogisticRegression() 
x_train = x_train.values.reshape(-1,1)
model.fit(x_train , y_train)
x_test = x_test.values.reshape(-1,1)
y_predicted = model.predict(x_test)
y_predicted
mode_score=model.score(x_test,y_test)
print(mode_score)

