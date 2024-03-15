from typing import List, Tuple
import pandas as pd
import datetime
#file_path = "farmers-protest-tweets-2021-2-4.json"


#@profile   #se puede descomentar para correr la función en la terminal con python -m memory_profiler q1_time.py y ver el uso de memoria.

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Cargar el archivo JSON en un DataFrame de Pandas
    #df = pd.read_json(file_path, lines=True)
    
    # Extraer el 'username' de la columna 'user'
    df['username'] = df['user'].apply(lambda user: user['username'])
    
    # Convertir la columna 'date' a datetime.date
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    # Agrupar por fecha y contar los tweets
    tweet_counts = df.groupby(df['date'])['id'].count().reset_index()
    
    # Ordenar por el conteo de tweets descendente y obtener las 10 fechas principales
    top_dates = tweet_counts.sort_values('id', ascending=False).head(10)['date'].tolist()
    
    # Encontrar el usuario con más tweets para cada fecha principal
    top_users = []
    for date in top_dates:
        date_df = df[df['date'] == date]
        top_user = date_df.groupby('username')['id'].count().sort_values(ascending=False).index[0]
        top_users.append((date, top_user))
    
    return top_users