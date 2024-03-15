from typing import List, Tuple
import datetime
from collections import Counter, defaultdict
import json
file_path = "farmers-protest-tweets-2021-2-4.json"

#@profile   #se puede descomentar para correr la función en la terminal con python -m memory_profiler q1_time.py y ver el uso de memoria.
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Inicializar contadores para contar tweets por fecha y por usuario
    tweet_counts = Counter()
    user_counts = defaultdict(Counter)
    
    # Leer el archivo JSON línea por línea
    with open(file_path, 'r') as f:
        for line in f:
            # Cargar cada línea como un objeto JSON
            tweet = json.loads(line)

            # Obtener la fecha y el usuario del tweet actual
            date = datetime.datetime.fromisoformat(tweet['date']).date()
            user = tweet['user']['username']
            
            # Incrementar el contador de tweets para la fecha actual
            tweet_counts[date] += 1

            # Incrementar el contador de tweets para el usuario actual en la fecha actual
            user_counts[date][user] += 1
    
    # Obtener las top 10 fechas con más tweets
    top_dates = [date for date, count in tweet_counts.most_common(10)]
    
    # Para cada fecha en las top 10, encontrar el usuario con más tweets
    top_users = [(date, max(user_counts[date], key=user_counts[date].get)) for date in top_dates]
    
    return top_users