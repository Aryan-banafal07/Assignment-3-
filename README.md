# Assignment-3-
Exploratory Data Analysis on the Iris Dataset

📊 Exploratory Data Analysis on the Iris Dataset
📁 Dataset Overview
The Iris dataset contains measurements of 150 iris flowers from three species: setosa, versicolor, and virginica. Each entry includes:

Sepal length and width

Petal length and width

Species label

We further engineered two new features:

Petal area = petal length × petal width

Sepal area = sepal length × sepal width

We also binned petal length into categories: Very Short, Short, Medium, Long.

📈 Visualizations & Key Insights
1. Petal Length Over Samples
The petal length increases steadily across samples with some variation between species.

2. Histogram of Sepal Width
Most sepal widths fall between 2.5 and 3.5 cm.

A slight right skew suggests more flowers with smaller widths.

3. Species Distribution (Pie Chart)
The dataset is balanced: each species (setosa, versicolor, virginica) accounts for ~33.3%.

4. Petal Length Group Distribution
Short and Medium lengths are most common.

Very few flowers have Very Short or Long petals.

5. Sepal Length by Species (Boxplot)
Virginica has the highest median sepal length.

Setosa is clearly distinct with shorter sepals.

6. Average Petal Area by Species
Virginica has the largest petal area, followed by versicolor, then setosa.

This suggests a strong species–petal size relationship.

7. Sepal Width by Species
Setosa tends to have the widest sepals on average.

8. Petal Length Category Counts
Majority of flowers fall into Short and Medium categories.

9. Average Sepal Area by Petal Length Group
Flowers with longer petals tend to have larger sepals as well — shows correlated growth.

✅ Conclusion
This EDA confirms the clear separation between Iris species based on petal and sepal dimensions, both in terms of area and categorical grouping. It also reveals that petal length is a strong differentiator across the classes and correlates well with sepal dimensions.
