import pandas as pd
from pymongo import MongoClient
import json

def get_db_connection():
    # Establish a connection to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    
    # Access the specific database (it will be created if it doesn't exist)
    db = client["company_analytics"]
    return db

def ingest_data():
    print("Starting data ingestion...")

    # Read the Excel file into a DataFrame
    df = pd.read_excel('../data/raw/company_data.xlsx')
    
    # Convert 'Order Date' to string format to ensure compatibility with MongoDB
    df['Order Date'] = df['Order Date'].astype(str)

    # Convert the DataFrame to a list of dictionaries (records)
    records = df.to_dict(orient='records')
    
    print(f"Number of records to ingest: {len(records)}")
    
    # Connect to MongoDB and insert the records
    db = get_db_connection()
    collection = db["orders"]
    
    # Clear existing data in the collection before inserting new records
    collection.drop() 
    
    print("Inserting records into MongoDB...")
    # Insert the records into the MongoDB collection
    collection.insert_many(records)

    # Verify the insertion by counting the documents in the collection
    count = collection.count_documents({})
    print(f"Data ingestion completed. Total records in MongoDB: {count}")
    
if __name__ == "__main__":
    ingest_data()