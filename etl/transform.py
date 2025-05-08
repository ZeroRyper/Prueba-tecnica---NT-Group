# Transformación al esquema
import pandas as pd
df = pd.read_parquet('./dataset/extracted.parquet')
df = df.rename(columns={
    'empresa': 'company_name',
    'empresa_id': 'company_id',
    'estado': 'status',
    'monto': 'amount',
    'creado': 'created_at',
    'actualizado': 'updated_at'
})
df['id'] = df.index.astype(str).str.zfill(24)
df.to_csv('./dataset/transformed.csv', index=False)
