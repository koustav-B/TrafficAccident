import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster

# Sample data (replace this with your actual data)
df = pd.read_excel('accident_data.xlsx')

# Summary statistics
summary_stats = df.describe()
print("Summary Statistics:")
print(summary_stats)

# Accident counts by weather conditions
weather_counts = df['Weather'].value_counts()
print("\nAccident counts by weather conditions:")
print(weather_counts)

# Accident counts by road conditions
road_conditions_counts = df['Road_Conditions'].value_counts()
print("\nAccident counts by road conditions:")
print(road_conditions_counts)

# Accident counts by accident severity
severity_counts = df['Accident_Severity'].value_counts()
print("\nAccident counts by accident severity:")
print(severity_counts)

# Accident counts by contributing factors
factor_counts = df['Contributing_Factor'].value_counts()
print("\nAccident counts by contributing factors:")
print(factor_counts)

# Plot accident counts by weather conditions
plt.figure(figsize=(12, 6))
sns.barplot(x=weather_counts.index, y=weather_counts.values, hue=weather_counts.index, legend=False, palette='viridis')
plt.title('Accident Counts by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plot accident counts by road conditions
plt.figure(figsize=(12, 6))
sns.barplot(x=road_conditions_counts.index, y=road_conditions_counts.values, hue=road_conditions_counts.index, legend=False, palette='viridis')
plt.title('Accident Counts by Road Conditions')
plt.xlabel('Road Conditions')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plot accident counts by accident severity
plt.figure(figsize=(8, 5))
sns.barplot(x=severity_counts.index, y=severity_counts.values, hue=severity_counts.index, legend=False, palette='viridis')
plt.title('Accident Counts by Severity')
plt.xlabel('Severity')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plot accident counts by contributing factors
plt.figure(figsize=(10, 6))
sns.barplot(x=factor_counts.index, y=factor_counts.values, hue=factor_counts.index, legend=False, palette='viridis')
plt.title('Accident Counts by Contributing Factors')
plt.xlabel('Contributing Factors')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Longitude', y='Latitude', hue='Accident_Severity', data=df, palette='viridis')
plt.title('Scatter Plot of Accidents')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Pie Chart for Accident Severity
plt.figure(figsize=(8, 8))
plt.pie(severity_counts, labels=severity_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis'))
plt.title('Distribution of Accident Severity')
plt.show()

# Density Plot
plt.figure(figsize=(12, 6))
sns.kdeplot(x=df['Longitude'], y=df['Latitude'], cmap='viridis', fill=True, thresh=0, levels=30)
plt.title('Density Plot of Accidents')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Sampling Theory
# Sample size for random sampling
sample_size = 30

# Check if the sample size is greater than the population size
if sample_size > len(df):
    print(f"Sample size ({sample_size}) cannot be greater than the population size ({len(df)}). Reducing sample size.")
    sample_size = len(df) - 1

sampled_df = df.sample(n=sample_size, replace=True, random_state=42)

# Display the sampled data
print(f"\nSampled Data (Size: {sample_size}):")
print(sampled_df)
