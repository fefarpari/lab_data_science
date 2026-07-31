import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\E2_10\e2_ds_10\sales_data.csv")
plt.plot(df["Month"],df["Sales"],marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()