import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
import os

os.makedirs('../results/charts', exist_ok=True)

def get_db_connection():
    client = MongoClient("mongodb://localhost:27017/")
    return client["company_analytics"]

# Visualize the results from the MapReduce jobs
def visualize_results():
    db = get_db_connection()
    
    # Visualize Total Profit by Sales Channel
    print('Visualizing Total Profit by Sales Channel')
    channel_data = list(db["results_channel_profit"].find())
    df_channel = pd.DataFrame(channel_data)
    
    # Rename columns for better readability
    df_channel.rename(columns={'_id': 'Channel', 'value': 'Total Profit'}, inplace=True)
    
    # Create a bar plot for Total Profit by Sales Channel
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_channel, x='Channel', y='Total Profit', palette='viridis')
    plt.title('Total Profit by Sales Channel')
    plt.xlabel('Sales Channel')
    plt.ylabel('Total Profit ($)')
    
    # Save the plot
    plt.savefig('../results/charts/channel_profit.png')
    plt.close()
    print('Total Profit by Sales Channel visualization saved.')

    # Visualize Total Order Quantity by Region and Product Category
    print('Visualizing Total Order Quantity by Region and Product Category')
    geo_data = list(db["results_geo_demand"].find())
    df_geo = pd.DataFrame(geo_data)
    
    # Split the '_id' column into 'Region' and 'Category'
    df_geo[['Region', 'Category']] = df_geo['_id'].str.split(' - ', expand=True)
    df_geo.rename(columns={'value': 'Total Quantity'}, inplace=True)
    
    # Create a pivot table for the heatmap
    pivot_geo = df_geo.pivot(index='Region', columns='Category', values='Total Quantity')
    
    # Create a heatmap for Total Order Quantity by Region and Product Category
    plt.figure(figsize=(14, 8))
    sns.heatmap(pivot_geo, annot=True, fmt=".0f", cmap='coolwarm', linewidths=.5)
    plt.title('Product Category Demand by Region')
    plt.xlabel('Product Category')
    plt.ylabel('Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('../results/charts/geo_demand_heatmap.png')
    plt.close()
    print('Total Order Quantity by Region and Product Category visualization saved.')

if __name__ == "__main__":
    visualize_results()