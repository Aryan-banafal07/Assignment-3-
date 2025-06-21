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

#OUTPUT: 



![image](https://github.com/user-attachments/assets/3d95e20c-c8fc-4aae-8c67-594e13e0c2f3)

![image](https://github.com/user-attachments/assets/5ab6479e-f6d2-444f-9844-94058d764294)

![image](https://github.com/user-attachments/assets/86e3bdba-7058-43f9-9bd9-fc94cbc04629)

![image](https://github.com/user-attachments/assets/e2630699-57ab-4463-b8ff-db2b497dd17b)

![image](https://github.com/user-attachments/assets/2552eb00-3bc8-4ad7-8e39-4bc19e6c71db)

![image](https://github.com/user-attachments/assets/a54f4263-0cae-40d4-a9af-7780c5af5d51)

![image](https://github.com/user-attachments/assets/bec30f60-c17a-4bb3-8852-d9ea20f58569)

![image](https://github.com/user-attachments/assets/603c97ec-c4ff-43ee-a456-49df0e2e77b1)

![image](https://github.com/user-attachments/assets/28eadfbe-8925-4f9c-84a6-4210269173d9)


Mean Petal Area by Species:
 species
setosa         0.3656
versicolor     5.7204
virginica     11.2962
Name: petal area, dtype: float64

Mean Sepal Width by Species:
 species
setosa        3.428
versicolor    2.770
virginica     2.974
Name: sepal width (cm), dtype: float64

Mean Sepal Area by PetalLength Group:
 PetalLengthGroup
Very Short    17.257800
Short         13.683125
Medium        18.360533
Long          23.841111
