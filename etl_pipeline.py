import pandas as pd
from sqlalchemy import create_engine

CSV_FILE = 'DataCoSupplyChainDataset.csv'
DB_NAME = 'supply_chain_db.sqlite'

def run_etl():
    try:
        df = pd.read_csv(CSV_FILE, encoding='latin-1')
        
        # FIX: Also remove parentheses '(' and ')'
        df.columns = [col.lower().replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '') for col in df.columns]
        
        df['order_zipcode'] = df['order_zipcode'].fillna(0)
        
        date_cols = ['order_date_dateorders', 'shipping_date_dateorders']
        for col in date_cols:
            df[col] = pd.to_datetime(df[col])

        if 'late_delivery_risk' in df.columns:
            df['late_delivery_risk'] = df['late_delivery_risk'].astype(int)

        engine = create_engine(f'sqlite:///{DB_NAME}')
        
        df.to_sql('supply_chain_data', engine, if_exists='replace', index=False)
        print("Data loaded successfully.")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    run_etl()