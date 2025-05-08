# Inserción en charges y companies
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://usuario:19460633@localhost:5432/etl_test")
df = pd.read_csv('./dataset/transformed.csv')
companies = df[['company_id', 'company_name']].drop_duplicates()
companies.to_sql('companies', engine, if_exists='append', index=False)
df.drop(columns=['company_name'], inplace=True)
df.to_sql('charges', engine, if_exists='append', index=False)
