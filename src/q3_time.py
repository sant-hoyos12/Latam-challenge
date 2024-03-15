from typing import List, Tuple
import pandas as pd
file_path = "farmers-protest-tweets-2021-2-4.json"


#@profile  #se puede descomentar para correr la función en la terminal con python -m memory_profiler q1_time.py y ver el uso de memoria.
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Cargar el archivo JSON en un DataFrame de Pandas
    #df = pd.read_json(file_path, lines=True)
    
    # Extraer las menciones de la columna 'mentionedUsers'
    df['mentions'] = df['mentionedUsers'].apply(lambda x: [user['username'] for user in x] if isinstance(x, list) else [])
    
    # Aplanar la lista de listas de menciones
    mentions = [mention for mentions in df['mentions'] for mention in mentions]
    
    # Contar las menciones por usuario
    mention_counts = pd.Series(mentions).value_counts()
    
    # Obtener los 10 usuarios con más menciones
    top_users = mention_counts.head(10).reset_index()
    top_users.columns = ['username', 'count']
    
    return list(top_users.itertuples(index=False, name=None))
