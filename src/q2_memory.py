from typing import List, Tuple
import emoji
import json
from collections import Counter
from emoji import emoji_list
file_path = "farmers-protest-tweets-2021-2-4.json"


#@profile   #se puede descomentar para correr la función en la terminal con python -m memory_profiler q1_time.py y ver el uso de memoria.
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = Counter()  # Inicializar un contador para los emojis

    with open(file_path, 'r') as f:   # Abrir el archivo JSON
        for line in f:   # Leer cada línea del archivo JSON
            tweet = json.loads(line)   # Parsear el tweet desde JSON
            content = tweet['content']   # Obtener el contenido del tweet

            # Se obtienen los emojis
            emojis = [emoji['emoji'] for emoji in emoji_list(content)]
            
            # Se actualiza el contador con los emojis que se encontraron.
            emoji_counts.update(emojis)

    top_emojis = emoji_counts.most_common(10)   # Obtener los 10 emojis más comunes junto con su conteo

    return top_emojis