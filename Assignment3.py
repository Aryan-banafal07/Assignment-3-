import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

df['petal area'] = df['petal length (cm)'] * df['petal width (cm)']
df['sepal area'] = df['sepal length (cm)'] * df['sepal width (cm)']

bins = [0, 2, 4, 6, 10]
labels = ['Very Short', 'Short', 'Medium', 'Long']
df['PetalLengthGroup'] = pd.cut(df['petal length (cm)'], bins=bins, labels=labels)

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['petal length (cm)'], color='green', alpha=0.7)
plt.title('Petal Length Across Samples')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title('Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(6,6))
df['species'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightgreen'])
plt.title('Species Distribution')
plt.ylabel('')
plt.show()

plt.figure(figsize=(6,6))
df['PetalLengthGroup'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Petal Length Group Distribution')
plt.ylabel('')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='species', y='sepal length (cm)', data=df, palette='Set2')
plt.title('Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.show()

plt.figure(figsize=(6,4))
df.groupby('species')['petal area'].mean().sort_values().plot(kind='bar', color='purple')
plt.ylabel('Average Petal Area')
plt.title('Mean Petal Area by Species')
plt.show()

plt.figure(figsize=(6,4))
df.groupby('species')['sepal width (cm)'].mean().plot(kind='bar', color='teal')
plt.ylabel('Avg Sepal Width')
plt.title('Sepal Width by Species')
plt.show()

plt.figure(figsize=(7,4))
df['PetalLengthGroup'].value_counts().plot(kind='bar', color='orange')
plt.ylabel('Count')
plt.title('Petal Length Category Counts')
plt.show()

plt.figure(figsize=(7,4))
df.groupby('PetalLengthGroup')['sepal area'].mean().plot(kind='bar', color='navy')
plt.ylabel('Avg Sepal Area')
plt.title('Avg Sepal Area by Petal Length Group')
plt.show()

print("Mean Petal Area by Species:\n", df.groupby('species')['petal area'].mean())
print("\nMean Sepal Width by Species:\n", df.groupby('species')['sepal width (cm)'].mean())
print("\nMean Sepal Area by PetalLength Group:\n", df.groupby('PetalLengthGroup')['sepal area'].mean())
