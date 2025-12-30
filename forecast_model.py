import pandas as pd
import sqlite3
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

DB_NAME = 'supply_chain_db.sqlite'

def run_forecasting():
    conn = sqlite3.connect(DB_NAME)
    
    query = """
    SELECT 
        strftime('%Y-%m', order_date_dateorders) as Month,
        SUM(sales_per_customer) as Revenue
    FROM supply_chain_data
    GROUP BY Month
    ORDER BY Month;
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()

    df['Month'] = pd.to_datetime(df['Month'])
    df['Month_Ordinal'] = df['Month'].map(pd.Timestamp.toordinal)

    X = df[['Month_Ordinal']]
    y = df['Revenue']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Model Training Complete. Mean Absolute Error: {mae:.2f}")

    last_date = df['Month'].max()
    future_dates = [last_date + pd.DateOffset(months=i) for i in range(1, 7)]
    future_ordinals = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)

    future_predictions = model.predict(future_ordinals)

    forecast_df = pd.DataFrame({
        'Date': future_dates,
        'Predicted_Revenue': future_predictions
    })

    combined_df = pd.concat([df[['Month', 'Revenue']], forecast_df.rename(columns={'Date': 'Month', 'Predicted_Revenue': 'Revenue'})])
    combined_df['Type'] = ['Actual'] * len(df) + ['Forecast'] * len(forecast_df)
    
    combined_df.to_csv('forecast_results.csv', index=False)
    print("Forecast generated. Saved to 'forecast_results.csv'.")

if __name__ == "__main__":
    run_forecasting()