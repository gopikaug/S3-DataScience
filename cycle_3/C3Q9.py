import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
sns.displot(iris['sepal_length'], kde=True)
plt.title("Univariate Distribution Plot (KDE) for Sepal Length")
plt.show()
sns.histplot(iris['sepal_width'], kde=True)
plt.title("Histogram for Sepal Width")
plt.show()
sns.relplot(x='sepal_length', y='sepal_width', data=iris, kind='scatter', hue='species')
plt.title("Relational Plot: Sepal Length vs Sepal Width (Colored by Species)")
plt.show()




