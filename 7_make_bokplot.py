import pandas as pd
import matplotlib.pyplot as plt
import os 
os.getcwd()           
# get current working directory
dataset = pd.read_csv(".\csv\exms.csv")
dataset  
dataset.columns
dataset.boxplot("age")
plt.show()
