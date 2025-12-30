# End-to-End-Supply-Chain-Analytics
# End-to-End Supply Chain Optimization & Demand Forecasting System

## 📌 Executive Summary
A full-stack data analytics solution designed to optimize inventory levels and predict future revenue for a global logistics company. This project integrates **Data Engineering (ETL)**, **SQL Analytics**, and **Machine Learning** to solve real-world business problems like stockouts, overstocking, and shipment delays.

**Business Impact:**
* **Reduced Risk:** Identified high-risk products with >90% late delivery rates.
* **Improved Forecasting:** Built a Linear Regression model to predict sales trends for the next 6 months.
* **Data Pipeline:** Automated the transformation of raw CSV logs into a structured SQL database.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.10+
* **Database:** SQLite (SQLAlchemy for ORM)
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Visualization:** Power BI (Dashboarding)
* **IDE:** VS Code

---

## 🏗️ System Architecture
The project follows a modular "production-ready" pipeline structure:

1.  **ETL Pipeline (`etl_pipeline.py`)**:
    * Extracts raw supply chain logs (`.csv`).
    * Cleans data (removes special characters, fixes datetime formats).
    * Loads structured data into a SQL Database.

2.  **Analytics Engine (`analysis_queries.py`)**:
    * Executes complex SQL queries to calculate KPIs (Revenue by Region, Late Delivery Risk).
    * Exports aggregated reports for the BI Dashboard.

3.  **Predictive Model (`forecast_model.py`)**:
    * Trains a Linear Regression model on historical sales data.
    * Generates a 6-month future revenue forecast.

---

## 📊 Key Insights & Results

### 1. Regional Performance
* Identified top-performing regions driving 60% of total revenue.
* **Action:** Recommended inventory reallocation to these high-demand zones to reduce shipping times.

### 2. Supply Chain Risk
* Analyzed "Late Delivery Risk" across all product categories.
* **Finding:** Specific product categories had a consistently high delay rate, flagging a need for vendor review.

### 3. Demand Forecast
* The Machine Learning model identified a steady growth trend for the upcoming quarter.
* **Utility:** Allows the procurement team to stock up 3 months in advance, preventing potential stockouts.

---

## 🚀 How to Run This Project

### Prerequisites
* Python 3.x
* Power BI Desktop (for visualization)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/SupplyChain_Project.git](https://github.com/YOUR_USERNAME/SupplyChain_Project.git)
    cd SupplyChain_Project
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas numpy sqlalchemy scikit-learn
    ```

3.  **Run the Pipeline:**
    ```bash
    # Step 1: Initialize Database & Load Data
    python etl_pipeline.py

    # Step 2: Run SQL Analytics
    python analysis_queries.py

    # Step 3: Generate Forecasts
    python forecast_model.py
    ```

4.  **View Dashboard:**
    * Open `SupplyChain_Dashboard.pbix` in Power BI Desktop to interact with the visualizations.

---

## 📂 Project Structure
```text
├── DataCoSupplyChainDataset.csv  # Raw Data Source
├── etl_pipeline.py               # Data Engineering (Extract-Transform-Load)
├── analysis_queries.py           # SQL Business Analysis
├── forecast_model.py             # ML Prediction Script
├── supply_chain_db.sqlite        # Generated Database
├── forecast_results.csv          # ML Model Output
└── README.md                     # Project Documentation
