# Global Tuberculosis Incidence Analysis: End-to-End Pipeline

An end-to-end data engineering and analytics project that tracks, cleans, and visualizes global Tuberculosis (TB) incidence rates from 2000 to 2024. This project demonstrates a full data pipeline: ingesting live data from the World Bank API, processing it with Python, and delivering actionable insights via an interactive Tableau dashboard.

Data Source: [World Bank Open Data API](https://api.worldbank.org/v2/country/all/indicator/SH.TBS.INCD?format=json&per_page=1000)

## 🎯 Project Objective
To analyze global tuberculosis incidence trends using data from the World Bank API and present key public health insights through an interactive Tableau dashboard.

## 🛠️ Tech Stack & Workflow
* **Data Ingestion:** Python (`requests` library) to query and pull data from the World Bank API.
* **Data Cleaning & ETL:** Python (`pandas`) to handle missing values, format data types, filter out unneeded regions, and reshape the schema for BI compatibility.
* **Exploratory Data Analysis (EDA):** Python (`matplotlib`) to discover initial data distributions and outliers.
* **Data Visualization:** Tableau Desktop to design the dashboard.

## 📊 Key Findings 
* **Global Trend Analysis:** Global average TB incidence has steadily declined from 2000 to 2024.
* **South Africa Analysis::** South Africa experienced significantly elevated TB incidence during the early 2000s before showing gradual improvement after 2014.
* **Most Recent Highest Incidence Rate:** Kiribati recorded the highest TB incidence among reporting countries in 2024.

## Dashboard Preview
<img width="1440" height="809" alt="Global_TB_Incidence_Dashboard" src="https://github.com/user-attachments/assets/f6e4912f-6b8c-4e0e-b2a0-ee3e50140d31" />

## Skills Demonstrated

- API Integration
- Data Cleaning & Transformation
- Exploratory Data Analysis
- Data Visualization
- Dashboard Development
- ETL Pipeline Design
- Public Health Analytics

## 📁 Repository Structure
* `/data/` - Cleaned CSV file.
* `/scripts/` - Python script for API ingestion, data cleaning, exploratory analysis, and ETL processing.
* `/tableau/` - The packaged Tableau Workbook (`.twbx`).

## 🚀 How to Run the Project
1. **Clone the repository:** `git clone https://github.com`
2. **Run the ETL pipeline:** Install dependencies via `pip install -r requirements.txt` and execute `python scripts/main.py`.
3. **View the Dashboard:** Open the `.twbx` file in Tableau Desktop/Public, or view it directly on [View Interactive Dashboard on Tableau Public](https://public.tableau.com/views/GlobalTBSurveillanceDashboard/GlobalTBSurveillanceDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
