import pandas as pd
import sqlite3

DB_NAME = 'supply_chain_db.sqlite'

def run_analysis():
    conn = sqlite3.connect(DB_NAME)
    
    q1 = """
    SELECT 
        order_region as Region,
        SUM(sales_per_customer) as Total_Revenue,
        COUNT(order_id) as Total_Orders
    FROM supply_chain_data
    GROUP BY order_region
    ORDER BY Total_Revenue DESC;
    """
    
    q2 = """
    SELECT 
        product_name,
        COUNT(*) as Total_Orders,
        SUM(late_delivery_risk) as Late_Count,
        ROUND((CAST(SUM(late_delivery_risk) AS FLOAT) / COUNT(*)) * 100, 2) as Late_Percentage
    FROM supply_chain_data
    GROUP BY product_name
    HAVING COUNT(*) > 50
    ORDER BY Late_Percentage DESC
    LIMIT 10;
    """
    
    # FIX: Updated column name to remove parentheses
    q3 = """
    SELECT 
        strftime('%Y-%m', order_date_dateorders) as Month,
        SUM(sales_per_customer) as Revenue
    FROM supply_chain_data
    GROUP BY Month
    ORDER BY Month;
    """

    try:
        df_region = pd.read_sql_query(q1, conn)
        df_region.to_csv('analysis_region_revenue.csv', index=False)

        df_late = pd.read_sql_query(q2, conn)
        df_late.to_csv('analysis_late_risk.csv', index=False)
        
        df_time = pd.read_sql_query(q3, conn)
        df_time.to_csv('analysis_monthly_revenue.csv', index=False)
        
        print("Analysis complete. CSV files created.")

    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    run_analysis()