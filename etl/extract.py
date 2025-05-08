# Extracción a Parquet
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://usuario:19460633@localhost:5432/etl_test")
df = pd.read_sql('SELECT * FROM raw_purchases', engine)
df.to_parquet('./dataset/extracted.parquet', index=False)
