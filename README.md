# Zomato Restaurant Data Analysis Using Python

Understanding customer preferences and restaurant trends is crucial for making informed business decisions in the food industry. This project performs an Exploratory Data Analysis (EDA) on Zomato's restaurant dataset using Python to uncover key insights.

## 📋 Objectives
This analysis aims to answer the following questions:
1. **Do more restaurants provide online delivery compared to offline services?**
2. **Which types of restaurants are most favored by the general public?**
3. **What price range do couples prefer for dining out?**

---

## 📂 Project Structure
* `Zomato-data-.csv`: The dataset containing 148 restaurant records with their online availability, booking options, customer ratings, votes, dining costs, and categories.
* `zomato_data.py`: The Python analysis script that cleans the dataset, runs statistical queries, outputs key findings, and generates visualization plots.
* `README.md`: Documentation of the project (this file).

---

## 🔧 Prerequisites & Setup
Make sure you have Python 3 installed, along with the required libraries.

You can install the necessary dependencies using `pip`:
```bash
pip install pandas numpy matplotlib seaborn
```

---

## 🚀 How to Run the Analysis
To execute the analysis, run the following command in your terminal:
```bash
python zomato_data.py
```

### Script Execution Outputs:
1. **Console Output:** The script prints data cleaning steps, dataset summaries, and explicit answers to the three core questions.
2. **Saved Visualizations (PNG):**
   * `online_vs_offline_count.png`: A count plot comparing restaurants offering online vs. offline orders.
   * `votes_by_restaurant_type.png`: A line chart displaying the total customer votes across restaurant categories.
   * `couple_dining_cost_distribution.png`: A count plot showing the distribution of approximate dining costs for two people.
   * `ratings_distribution.png`: A histogram depicting the distribution of customer ratings.
   * `online_vs_offline_ratings_boxplot.png`: A boxplot comparing restaurant ratings between online and offline ordering categories.
   * `type_vs_online_order_heatmap.png`: A heatmap illustrating the relationship between restaurant types and online delivery options.

---

## 🔍 Core Findings

### 1. Online Delivery vs. Offline Services
* **Verdict:** More restaurants offer offline services compared to online delivery.
* **Details:** 90 restaurants (60.8%) operate offline-only, while 58 restaurants (39.2%) accept online orders.

### 2. Restaurant Popularity (Favored Types)
* **Verdict:** **Dining** type restaurants are heavily favored by the general public in terms of overall interaction (votes).
* **Details:** Dining restaurants accumulated **20,363 votes** in total. The most voted individual restaurant is `Empire Restaurant` with **4,884 votes**.

### 3. Price Preferences for Couples
* **Verdict:** Couples prefer budget-friendly options, with **300 Rupees** for two people being the single most common price range (offered by 23 restaurants).

---
