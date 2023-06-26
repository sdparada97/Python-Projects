from typing import Dict
from requests import get, exceptions
from functools import lru_cache

class PokeAPI:

    def __init__(self) -> None:
        self.base_url = "https://pokeapi.co/api/v2"

    def get_list_pokemons(self) -> Dict[str,any]:
        params = {'limit' : 10,'offset' : 0} 
        try:
            response = get(f'{self.base_url}/pokemon',params=params)
            
            if response.status_code == 200:
                poke_data = response.json()
                return (poke_data["results"])
            else:
                print(f"La API devolvio un error: {response.status_code}")
                
        except exceptions.RequestException as e:
            print(f"Ocurrio un error: {e}")

    @lru_cache(maxsize=10)
    def get_pokemon_by_id(self,id) -> Dict[str,any]:
        try:
            response = get(f'{self.base_url}/pokemon/{id}/')

            if response.status_code == 200:
                poke_data = response.json()
                return {
                    "id": poke_data["id"],
                    "name": poke_data["name"],
                    "types": poke_data["types"],
                }
            else:
                print(f"La API devolvio un error: {response.status_code}")

        except exceptions.RequestException as e:
            print(f"Ocurrio un error: {e}")
