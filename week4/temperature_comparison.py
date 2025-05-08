
import pandas as pd
import matplotlib.pyplot as plt

# path
auckland_file = "1962__monthly__Mean_air_temperature__Deg_C.csv"
christchurch_file = "44763__monthly__Mean_air_temperature__Deg_C.csv"

# load data 
auckland_df = pd.read_csv(auckland_file)
christchurch_df = pd.read_csv(christchurch_file)

# filter 2022 data
auckland_2022 = auckland_df[auckland_df['YEAR'] == 2022].reset_index(drop=True)
christchurch_2022 = christchurch_df[christchurch_df['YEAR'] == 2022].reset_index(drop=True)

# merge data in to one df
comparison_df = pd.DataFrame({
    'Month': auckland_2022['PERIOD'],
    'Auckland': auckland_2022['STATS_VALUE'],
    'Christchurch': christchurch_2022['STATS_VALUE']
})

# calculate difference
comparison_df['Difference'] = comparison_df['Auckland'] - comparison_df['Christchurch']

# print data 
print(comparison_df)

# create plot
plt.figure(figsize=(10, 6))

# 
plt.plot(comparison_df['Month'], comparison_df['Auckland'], marker='o', label='Auckland', linestyle='-', linewidth=2)
plt.plot(comparison_df['Month'], comparison_df['Christchurch'], marker='o', label='Christchurch', linestyle='-', linewidth=2)

# 
plt.bar(comparison_df['Month'], comparison_df['Difference'], color='lightblue', alpha=0.6, label='Temperature Difference')

# title and details
plt.title('Monthly Average Temperature Comparison (2022) - Auckland vs Christchurch')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# show
plt.xticks(rotation=45)
plt.show()
