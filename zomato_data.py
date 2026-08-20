import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plotting style for clean aesthetics
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (8, 6)

# 1. Load the dataset (using correct local path)
csv_filename = "Zomato-data-.csv"
if not os.path.exists(csv_filename):
    raise FileNotFoundError(f"Dataset file '{csv_filename}' not found in the current directory.")

dataframe = pd.read_csv(csv_filename)
print("Initial Dataset Sample:")
print(dataframe.head())
print("\n" + "="*50 + "\n")

# 2. Data Cleaning and Preparation
def handleRate(value):
    value = str(value).split('/')
    value = value[0].strip()
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)

print("Dataset Info:")
dataframe.info()
print("\nNull Values Count:")
print(dataframe.isnull().sum())
print("\n" + "="*50 + "\n")

# 3. Exploratory Data Analysis & Answering Questions

# --- QUESTION 1: Do more restaurants provide online delivery compared to offline services? ---
online_order_counts = dataframe['online_order'].value_counts()
q1_answer = "No, more restaurants offer offline services compared to online delivery."
if online_order_counts.get('Yes', 0) > online_order_counts.get('No', 0):
    q1_answer = "Yes, more restaurants provide online delivery compared to offline services."

print("--- QUESTION 1 ANSWER ---")
print(f"Online Order Statistics:\n{online_order_counts.to_string()}")
print(f"Verdict: {q1_answer}\n")

# Plot Online vs Offline Order count
plt.figure()
sns.countplot(x='online_order', data=dataframe, hue='online_order', palette='Set2', legend=False)
plt.title("Online vs Offline Order Count")
plt.xlabel("Online Order Option")
plt.ylabel("Number of Restaurants")
plt.savefig("online_vs_offline_count.png", dpi=300, bbox_inches='tight')
plt.close()

# --- QUESTION 2: Which types of restaurants are most favored by the general public? ---
# Group by type and sum the votes
votes_by_type = dataframe.groupby('listed_in(type)')['votes'].sum().sort_values(ascending=False)
most_favored_type = votes_by_type.index[0]
most_favored_votes = votes_by_type.iloc[0]

print("--- QUESTION 2 ANSWER ---")
print(f"Total Votes by Restaurant Type:\n{votes_by_type.to_string()}")
print(f"Verdict: '{most_favored_type}' restaurants are most favored by the general public (received {most_favored_votes:,} votes in total).\n")

# Plot Votes by Restaurant Type
plt.figure()
plt.plot(votes_by_type.index, votes_by_type.values, c='green', marker='o', linewidth=2, markersize=8)
plt.title("Votes by Restaurant Type")
plt.xlabel("Type of Restaurant")
plt.ylabel("Total Votes")
plt.savefig("votes_by_restaurant_type.png", dpi=300, bbox_inches='tight')
plt.close()

# Let's also print the restaurant with the maximum votes overall
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name'].values[0]
print(f"Restaurant with the absolute maximum votes overall: '{restaurant_with_max_votes}' ({max_votes:,} votes)\n")

# --- QUESTION 3: What price range do couples prefer for dining out? ---
couple_data = dataframe['approx_cost(for two people)']
cost_counts = couple_data.value_counts().sort_values(ascending=False)
preferred_cost = cost_counts.index[0]
preferred_cost_count = cost_counts.iloc[0]

print("--- QUESTION 3 ANSWER ---")
print("Approximate Dining Cost Counts (for two people):")
print(cost_counts.head(5).to_string())
print(f"Verdict: Couples prefer restaurants with an approximate cost of {preferred_cost} rupees for two people (preferred by {preferred_cost_count} restaurants).\n")

# Plot Approximate Cost for Two
plt.figure()
sns.countplot(x='approx_cost(for two people)', data=dataframe, hue='approx_cost(for two people)', palette='viridis', legend=False)
plt.title("Approximate Cost Distribution for Two People")
plt.xlabel("Approximate Cost (Rupees)")
plt.ylabel("Number of Restaurants")
plt.savefig("couple_dining_cost_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# --- OTHER INSIGHTS & VISUALIZATIONS ---

# 4. Rating Distribution
plt.figure()
plt.hist(dataframe['rate'], bins=5, color='skyblue', edgecolor='black')
plt.title('Ratings Distribution')
plt.xlabel('Rating (out of 5)')
plt.ylabel('Number of Restaurants')
plt.savefig("ratings_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 5. Rating Comparison: Online vs Offline Boxplot
plt.figure(figsize=(6, 6))
sns.boxplot(x='online_order', y='rate', data=dataframe, hue='online_order', palette='Pastel1', legend=False)
plt.title('Ratings Comparison - Online vs Offline Orders')
plt.xlabel('Online Order Option')
plt.ylabel('Rating')
plt.savefig("online_vs_offline_ratings_boxplot.png", dpi=300, bbox_inches='tight')
plt.close()

# 6. Heatmap of Restaurant Type vs Online Order Option
plt.figure(figsize=(8, 6))
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d', cbar_kws={'label': 'Count'})
plt.title('Restaurant Count: Type vs Online Order Option')
plt.xlabel('Online Order Option')
plt.ylabel('Listed In (Type)')
plt.savefig("type_vs_online_order_heatmap.png", dpi=300, bbox_inches='tight')
plt.close()

print("="*50)
print("Analysis Complete! All answer summaries have been printed, and 6 visualization plots have been saved as PNG files in the current folder.")
print("="*50)