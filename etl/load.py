import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Cargar el dataset
df = pd.read_csv('./dataset/data_prueba_tecnica.csv')

try:
    # Crear la conexión con la base de datos
    engine = create_engine("postgresql+psycopg2://usuario:19460633@localhost:5432/etl_test")
    
    with engine.connect() as conn:
        print("✅ Conexión exitosa")
    
    # Cargar los datos a la base de datos
    df.to_sql('raw_purchases', engine, if_exists='replace', index=False)
    print("✅ Datos cargados exitosamente")
    
except OperationalError as e:
    print("❌ Falló la conexión:", e)
except Exception as e:
    print("❌ Ocurrió un error inesperado:", e)
