import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target

data['species'] = data['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='sepal length (cm)', y='sepal width (cm)', hue='species', palette='deep')
plt.title('Диаграмма рассеяния для Iris Dataset')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Ширина чашелистика (см)')
plt.legend(title='Вид')
plt.show()
