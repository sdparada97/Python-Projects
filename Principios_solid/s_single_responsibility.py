"""
SINGLE RESPONSABILITY:
    A class should have only one reason to change.

"""
import csv
from pathlib import Path
from typing import List


class Pokemon:
    def __init__(self) -> None:
        self.name:str
        self.type:str
        self.skills:List[str]
        self.evolutions:List[str]

    def as_dict(self) -> dict:
        return {
            'name': self.name,
            'type': self.type,
            'skills': self.skills,
            'evolutions': self.evolutions
        }

"""
IN THIS SCRIPT, WE ARE SEPARATING TWO
CLASSES AND EACH ONE HAS ONE REASON TO CHANGE
"""

class Database_file:
    open('files/pokemones.csv','w').close()

    def save_data(self,pokemon: Pokemon):
        with open('files/pokemones.csv','w',newline='', encoding='utf-8') as file:
            headers = list(pokemon.as_dict().keys())
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerow(pokemon.as_dict())

        return "SAVE POKEMON !!"

if __name__ == '__main__':
    eeve = Pokemon()
    eeve.name = 'Eevee'
    eeve.type = 'Normal'
    eeve.evolutions = ['Vaporeon','Jolteon','Flareon']
    eeve.skills = ['Última baza','Ataque rápido']

    db = Database_file()
    db.save_data(eeve)