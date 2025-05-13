import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.datasets import co2

data = co2.load_pandas().data

print(data.head())

data = data.dropna()

data = data[data.index.year >= 1958]
data = data[data.index.year <= 1980]

plt.figure(figsize=(10, 5))
plt.plot(data.index, data['co2'], label='CO2 Levels', color='blue')
plt.title('Динамика уровней CO2 (1958–1980)')
plt.xlabel('Год')
plt.ylabel('Уровень CO2 (ppm)')
plt.legend()
plt.grid()
plt.show()
