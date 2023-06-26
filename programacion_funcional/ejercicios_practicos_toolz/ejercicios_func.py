from collections import Counter
from functools import partial
from poke_api import PokeAPI
from pprint import pprint
from toolz import get_in

api = PokeAPI()

""" 
Utiliza la función `cache` o `lru_cache` para decorar la función 
y almacenar en caché el resultado para entradas de argumentos repetidos
"""
print(f"Resultado: {get_in(['name'],api.get_pokemon_by_id(4))}")
print(f"Resultado: {get_in(['name'],api.get_pokemon_by_id(5))}")
print(f"Resultado: {get_in(['name'],api.get_pokemon_by_id(5))}")
print(f"Resultado: {get_in(['name'],api.get_pokemon_by_id(5))}")
print(f"Resultado: {get_in(['name'],api.get_pokemon_by_id(4))}")
print(f"Resultado: {get_in(['name'],api.get_pokemon_by_id(10))}")
print(api.get_pokemon_by_id.cache_info())


""" 
Crea una función que filtre los datos retornados por la API 
dado una llave y un valor (key: value) dado.

Crea funciones parciales con los filtros mas comunes.
"""
list_pokemons = [ api.get_pokemon_by_id(num) for num in range(1,10)]

def filter_pokemon_name(value,character):
    return value.startswith(character)

filter_pokemon_name_start_c = partial(filter_pokemon_name,character='c')
filter_pokemon_name_start_b = partial(filter_pokemon_name,character='b')
filter_pokemon_name_start_i = partial(filter_pokemon_name,character='i')

print("******************************************************************************")
pprint([poke for poke in list_pokemons if filter_pokemon_name_start_c(poke['name'])])
print("******************************************************************************")
pprint([poke for poke in list_pokemons if filter_pokemon_name_start_b(poke['name'])])
print("******************************************************************************")
pprint([poke for poke in list_pokemons if filter_pokemon_name_start_i(poke['name'])])
print("******************************************************************************")

""" 
Crea una función que dado una llave, retorne un diccionario
con los valores que puede tomar esa llave y la cantidad de cada uno
de ellos que hay en la respuesta de la API. 
Ej. 
count_by_key("difficulty") 
R/ {"Unknown": 3, "Advanced": 8, "Moderate": 1} 
"""
list_pokemons_api = api.get_list_pokemons()
pprint(list_pokemons_api)
print("******************************************************************************")

def count_by_key(key,list_dict=list_pokemons_api):
    list_values = [ poke[key] for poke in list_dict if key in poke ]
    return dict(Counter(list_values))

pprint(count_by_key('name'))
