from typing import List, Tuple
from collections import Counter
import json
file_path = "farmers-protest-tweets-2021-2-4.json"

#@profile  #se puede descomentar para correr la función en la terminal con python -m memory_profiler q1_time.py y ver el uso de memoria.
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Crear un objeto Counter para contar las menciones
    mention_counts = Counter()
    
    # Abrir el archivo y procesar cada línea
    with open(file_path, 'r') as f:
        for line in f:
            # Evaluar la línea como un diccionario de Python
            tweet = json.loads(line)
            
            # Extraer los usuarios mencionados de la columna 'mentionedUsers'
            mentions = [user['username'] for user in tweet['mentionedUsers']] if tweet['mentionedUsers'] else []
            
            # Actualizar el contador con las menciones de esta línea
            mention_counts.update(mentions)
    
    # Obtener los 10 usuarios con más menciones utilizando el método most_common
    top_users = mention_counts.most_common(10)
    
    return top_users