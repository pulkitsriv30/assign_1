import pandas as pd
import numpy as np

roll_number = 102303803

a_r = 0.05 * (roll_number % 7)
b_r = 0.3 * ((roll_number % 5) + 1)

df = pd.read_csv("data.csv", encoding="ISO-8859-1")

no2_col = "no2"

x = df[no2_col].fillna(df[no2_col].mean())

z = x + a_r * np.sin(b_r * x)

mu = z.mean()
sigma = z.std()

lam = 1 / (2 * sigma ** 2)
c = 1 / (sigma * np.sqrt(2 * np.pi))

print("mu =", mu)
print("lambda =", lam)
print("c =", c)
