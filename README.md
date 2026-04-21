# Big Data Analytics: Company Sales Performance

## Project Overview
This project is a comprehensive Big Data analytics pipeline developed as part of the Big Data course requirements. It demonstrates the ability to ingest, process, and analyze a real-world dataset of over 10,000 records using **MongoDB** for document-based data storage and **MapReduce** for distributed data processing.

## Tech Stack & Tools
* **Database:** MongoDB (Community Server & Compass)
* **Data Processing:** MongoDB MapReduce
* **Programming Language:** Python 3.x
* **Libraries:** `pandas`, `pymongo`, `matplotlib`, `seaborn`, `plotly`, `openpyxl`

## Project Structure
```text
big-data-company-analytics/
│
├── data/
│   └── company_data.xlsx              # Raw dataset (>15,000 records)
│
├── NoteBooks/
│   └── company-prediction-acc-96-with-data-analysis.ipynb # EDA & ML Notebook
│
├── src/
│   ├── data_ingestion.py              # Script to load Excel data into MongoDB
│   ├── map_reduce_jobs.py             # Script executing the 2 MapReduce jobs
│   └── data_visualization.py          # Script to generate charts from outputs
│
├── Results/
│   └── Charts/                        # Output visualizations (PNGs)
│
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

## MapReduce Jobs Implemented

To extract meaningful business intelligence from the raw sales data, two distinct MapReduce jobs were developed:

### 1. Channel Profitability Analysis
* **Map:** Extracts the `Sales Channel` as the key and `Profit` as the value.
* **Reduce:** Aggregates the total profit per channel to determine the most lucrative sales platforms.

### 2. Geo-Product Demand Analysis
* **Map:** Creates a composite key from `Region` and `Product Category`, emitting the `Order Quantity`.
* **Reduce:** Calculates the total volume of products demanded per region to guide targeted marketing.

---

## How to Run the Project

### 1. Prerequisites
* Ensure **MongoDB Community Server** is installed and running locally on the standard port `27017`.
* Install **MongoDB Compass** to visually inspect the data.

### 2. Environment Setup
Clone the repository and set up a virtual environment:

```bash
git clone <your-repository-url>
cd big-data-company-analytics

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 3. Execution Pipeline
Run the scripts in the following order from the `src/` directory:

```bash
cd src

# Step 1: Ingest Data into MongoDB (Creates 'company_analytics' DB)
python data_ingestion.py

# Step 2: Execute MapReduce Jobs (Creates output collections)
python map_reduce_jobs.py

# Step 3: Generate Visualizations (Saves charts to Results/Charts/)
python data_visualization.py
```
## Results
The processed data outputs are successfully visualized and saved in the Results/Charts/ directory, providing actionable business insights regarding regional demand and sales channel efficiency. These insights form the core of the final project presentation.