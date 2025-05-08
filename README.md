# Prueba-tecnica---NT-Group
Guia ejecucion 

docker-compose up -d

pip install -r requirements.txt
python etl/load.py
python etl/extract.py
python etl/transform.py
python etl/disperse.py

