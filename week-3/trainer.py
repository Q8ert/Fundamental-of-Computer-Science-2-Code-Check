#!/usr/bin/env python3

"""Trainer class for managing a team of Pokemon."""

from pokemon import Pokemon
from pokemon import WaterType
from pokemon import FireType


class Trainer:
    """A Pokemon trainer who manages a team of Pokemon."""


    def __init__(self, name: str) -> None:
        """Initialise a new Trainer."""
        self.max_team_size = 6
        self.name = name
        self.team = []
        

    def add_to_team(self, pokemon: Pokemon) -> bool:
        """Add a Pokemon to the trainer's team.

        Returns True if successful, False if team is full.
        """
        if len(self.team) == self.max_team_size:
            print(len(self.team), self.max_team_size)
            print(f"{self.name} has a full team")
            return False
        else:
            self.team.append(pokemon)
            return True
    def get_team_size(self) -> int:
        """Get the number of Pokemon in the team."""
        return len(self.team)

    def get_first_available(self) -> Pokemon | None:
        """Get the first non-fainted Pokemon in the team."""
        for i in self.team:
            if i.is_fainted() == False:
                return i.name
        return None

    def get_pokemon_by_type(self, pokemon_type: type) -> list[Pokemon]:
        """Get a list of all Pokemon in the team that are instances of pokemon_type."""
        fin = []
        for i in self.team:
            if isinstance(i, pokemon_type):
                fin.append(i.name)
        return fin
    
    def __str__(self) -> str:
        """Return a string representation of this Trainer."""
        return (f"{self.name} has {self.get_team_size()} Pokemons")

ash = Trainer("Ash")
ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
water_pokemon = ash.get_pokemon_by_type(WaterType)  # Returns [Squirtle]
print(water_pokemon)