from typing import List, Tuple
import pandas as pd
from emoji import emoji_list
from collections import Counter
file_path = "farmers-protest-tweets-2021-2-4.json"



#@profile   #se puede descomentar para correr la función en la terminal con python -m memory_profiler q1_time.py y ver el uso de memoria.
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON en un DataFrame de Pandas
    df = pd.read_json(file_path, lines=True)
    
    # Obtener un solo string que contenga todos los contenidos de los tweets
    single_string = df['content'].str.cat(sep=' ')
    
    # Usar el método emoji_list para analizar el string y obtener todos los emojis presentes
    emojis = [emoji['emoji'] for emoji in emoji_list(single_string)]
    
    # Contar los emojis y devolver los 10 más utilizados
    return Counter(emojis).most_common(10)
