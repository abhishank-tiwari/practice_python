import pandas as pd
import matplotlib.pyplot as plt
datta = pd.read_csv(".\csv\ennn.csv")
plt.scatter(datta["dstn"],datta["pric"])
plt.show()
