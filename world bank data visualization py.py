
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



country = pd.read_csv("/content/drive/MyDrive/Week 4 - World Bank Data/Metadata_Country.csv")
population = pd.read_csv("/content/drive/MyDrive/Week 4 - World Bank Data/country_population.csv")
fertility = pd.read_csv("/content/drive/MyDrive/Week 4 - World Bank Data/fertility_rate.csv")
life_expectancy = pd.read_csv("/content/drive/MyDrive/Week 4 - World Bank Data/life_expectancy.csv")



country.head()

""" Getting first 5 values of 'fertility' dataset"""

fertility.head()

"""- Getting first 5 values of 'population' dataset"""

population.head()

"""- Getting first 5 values of 'life_expectancy' dataset"""

life_expectancy.head()

"""- Creating a copy of dataset to prevent data-loss"""

country_copy = country.copy()
population_copy = population.copy()
fertility_copy = fertility.copy()
life_expectancy_copy = life_expectancy.copy()



columns_to_drop = ['IncomeGroup', 'SpecialNotes', 'TableName', 'Unnamed: 5']
country_copy.drop(columns=columns_to_drop, inplace=True)

"""- Getting the first 5 values of the dataset"""

country_copy.head()

"""- Getting info about the dataset"""

country_copy.info()

"""- Checking for total number of null values in the dataset"""

country_copy.isna().sum()

"""- Getting first 5 values of 'population' dataset"""

population_copy.head()

"""- Dropping columns that are not required in the 'population' dataset"""

columns_to_drop = ['Indicator Name', 'Indicator Code']
population_copy.drop(columns=columns_to_drop, inplace=True)

"""- Checking for total number of null values in the dataset"""

population_copy.isna().sum()

"""- Getting info about the dataset"""

population_copy.info()

"""- Replacing mean values of the columns with the NaN values"""

years = [str(year) for year in range(1960, 2017)]
population_copy[years] = population_copy[years].astype('float64')

# For loop to replace the mean value of column with the NaN values
for year in years:
    population_copy[year].fillna(population_copy[year].mean(), inplace=True)

# Displaying first 5 values of the dataset
population_copy.head()

"""- Checking again for null values"""

population_copy.isna().sum()

"""- Getting all the columns of the dataset"""

population_copy.columns

"""- Getting the shape of the dataset"""

population_copy.shape

"""- Melting the dataset"""

melted_population = pd.melt(population_copy,
        id_vars='Country Code',
        value_vars=years,
        var_name='Year',
        value_name='Population')

"""- Getting the shape of the melted dataset"""

melted_population.shape

"""- Getting first 5 columns of the melted dataset"""

melted_population.head()

"""- Merging the 'country' and 'population' dataset"""

country_and_population_merge = pd.merge(country_copy, melted_population,how='left',on='Country Code')

"""- Getting the first 5 values of the merged dataset"""

country_and_population_merge.head()

"""- Getting first 5 values of fertility_dataset"""

fertility_copy.head()

"""- Dropping column that are not required in the fertility dataset"""

columns_to_drop = ['Indicator Name', 'Indicator Code']
fertility_copy.drop(columns=columns_to_drop, inplace=True)

"""- Getting first 5 values of the 'fertility' dataset"""

fertility_copy.head()

"""- Checking for null values"""

fertility_copy.isna().sum()

"""- Replacing mean values of the columns with the NaN values"""

years = [str(year) for year in range(1960, 2017)]
fertility_copy[years] = fertility_copy[years].astype('float64')

# For loop to replace the mean value of column with the NaN values
for year in years:
    fertility_copy[year].fillna(fertility_copy[year].mean(), inplace=True)

# Displaying first 5 values of the dataset
fertility_copy.head()

"""- Checking again for the null values"""

fertility_copy.isna().sum()

"""- Melting the dataset"""

melted_fertility = pd.melt(fertility_copy,
        id_vars='Country Code',
        value_vars=years,
        var_name='Year',
        value_name='Fertility')

"""- Getting first 5 values of the melted dataset"""

melted_fertility.head()

"""- Merging the 'country-population' and 'fertility' dataset"""

country_population_fertility_merge = pd.merge(country_and_population_merge, melted_fertility, how='left', on = ['Country Code', 'Year'])

"""- Getting the first 5 values of the merged dataset"""

country_population_fertility_merge.head()

"""- Getting the last 5 values of the merged dataset"""

country_population_fertility_merge.tail()

"""- Getting first 5 values of the 'life-expectancy' dataset"""

life_expectancy.head()

"""- Dropping the columns that are not required in the 'life_expectancy' dataset"""

columns_to_drop = ['Indicator Name', 'Indicator Code']
life_expectancy_copy.drop(columns=columns_to_drop, inplace=True)

"""- Getting first 5 values of the 'life_expectancy' dataset"""

life_expectancy.head()

"""- Checking for null values in the dataset"""

life_expectancy_copy.isna().sum()

"""- Replacing mean values of the columns with the NaN values"""

years = [str(year) for year in range(1960, 2017)]
life_expectancy_copy[years] = life_expectancy_copy[years].astype('float64')

# For loop to replace the mean value of column with the NaN values
for year in years:
    life_expectancy_copy[year].fillna(life_expectancy_copy[year].mean(), inplace=True)

# Displaying first 5 values of the dataset
life_expectancy_copy.head()

"""- Checking again for the null values in the dataset"""

life_expectancy_copy.isna().sum()

"""- Melting the dataset"""

melted_life_expectancy = pd.melt(life_expectancy_copy,
        id_vars='Country Code',
        value_vars=years,
        var_name='Year',
        value_name='Life Expectancy')

"""- Getting the first 5 values of the melted dataset"""

melted_life_expectancy.head()

"""- Merging the 'country-population-fertility' and 'life_expectancy' dataset"""

country_population_fertility_life_expectancy_merge = pd.merge(country_population_fertility_merge, melted_life_expectancy, how='left', on = ['Country Code', 'Year'])

"""- Getting first 5 values of the merged dataset"""

country_population_fertility_life_expectancy_merge.head()

"""- Creating a copy of the merged dataset and naming it as 'merged_final'"""

merged_final = country_population_fertility_life_expectancy_merge.copy()

"""- Getting info about the 'merged_final' dataset"""

merged_final.info()

"""- Converting the 'Year' column of 'merged_final' dataset as of integer datatype"""

merged_final['Year'] = merged_final['Year'].astype(int)

"""- Getting info about the 'merged_final' dataset"""

merged_final.info()

"""## **Data Visualization**

- Visualizing population trends accross different regions
"""

avg_population = merged_final.groupby(['Region', 'Year'])['Population'].mean().reset_index()

plt.style.use('dark_background')
plt.figure(figsize=(16, 7))
for region in avg_population['Region'].unique():
    subset = avg_population[avg_population['Region'] == region]
    plt.plot(subset['Year'], subset['Population'], label=region, linestyle='-')

plt.title('Average Population Over Years by Region', color='white')
plt.xlabel('Year', color='white')
plt.ylabel('Average Population', color='white')
plt.legend(facecolor='black', edgecolor='white', labelcolor='white')
plt.grid(True, color='gray', linestyle='--', linewidth=0.3)

years = avg_population['Year'].unique()
plt.xticks(years[::2], rotation=45, color='white')
plt.yticks(color='white')

plt.show()

"""-	Visualizing fertility rate distribution accross different regions"""

avg_fertility_rate = merged_final.groupby('Region')['Fertility'].mean().reset_index()

plt.style.use('dark_background')
plt.figure(figsize=(16, 5))
plt.bar(avg_fertility_rate['Region'], avg_fertility_rate['Fertility'])
plt.title('Average Fertility Rate by Region')
plt.xlabel('Region')
plt.ylabel('Average Fertility Rate')
plt.xticks(rotation=45)
plt.grid(True, color='gray', linestyle='--', linewidth=0.4)
plt.show()

"""- Visulaising	life expectancy variation accross different regions"""

plt.style.use('dark_background')
plt.figure(figsize=(16, 7))
sns.lineplot(data=merged_final, x='Year', y='Life Expectancy', hue='Region', palette='Set2', errorbar=None)
plt.title('Life Expectancy Variation by Region Over Time')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.legend(facecolor='black', edgecolor='white', labelcolor='white')
plt.xticks(rotation=90)
plt.grid(True, color='gray', linestyle='--', linewidth=0.3)
plt.show()

"""- Creating a correlation Analysis"""

numerical_columns = merged_final.select_dtypes(include=['float64', 'int64']).columns

correlation_matrix = merged_final[numerical_columns].corr()

sns.set(style="white")

plt.figure(figsize=(12, 5))

cmap = sns.color_palette("YlOrBr", as_cmap=True)
sns.heatmap(correlation_matrix, cmap=cmap, vmax=.3, center=0,
            linewidths=.5, cbar_kws={"shrink": .5},
            annot=True, fmt=".2f", annot_kws={"size": 10, "color": 'black'})

plt.title('Correlation Heatmap of Numerical Columns')

plt.show()

"""- Creating animated Bubble Chart for Fertility vs Life Expectancy by Region"""

fig = px.scatter(merged_final,
                 x='Fertility',
                 y='Life Expectancy',
                 size='Population',
                 color='Region',
                 hover_name='Country Code',
                 animation_frame='Year',
                 animation_group='Country Code',
                 template='plotly_dark',
                 size_max=95,
                 range_x=[0, 10],
                 range_y=[20, 85],
                 title='Animated Bubble Chart: Fertility vs Life Expectancy by Region',
                 labels={'Fertility': 'Fertility', 'Life Expectancy': 'Life Expectancy', 'Population': 'Population', 'Region': 'Region', 'Country Code': 'Country Code'})

fig.update_layout(
    xaxis_title='Fertility',
    yaxis_title='Life Expectancy',
    legend_title='Region',
    hoverlabel=dict(
        bgcolor='white',
        font_size=12,
        font_family='Arial, sans-serif'))

fig.show()