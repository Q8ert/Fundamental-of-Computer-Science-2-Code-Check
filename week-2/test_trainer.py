from trainer import Trainer
from pokemon import Pokemon
from pokemon import WaterType
from pokemon import FireType

def test_FireType_in_Team():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
    assert ash.get_pokemon_by_type(FireType) == ['Charmander']

def test_WaterType_in_Team():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
    assert ash.get_pokemon_by_type(WaterType) == ['Squirtle']
    
def test_No_Type_in_Team():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
    assert ash.get_pokemon_by_type(WaterType) == []
    
def test_More_same_Type_in_Team():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Squirtle", 44, 9, 10, "Water Gun", 40, 0.5))
    assert ash.get_pokemon_by_type(FireType) == ['Charmander', 'Squirtle']
    
    
def test_add_to_team():
    ash = Trainer("Ash")
    assert ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2)) == True
    
def test_add_to_team_full():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    assert ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2)) == False
    
def test_get_team_size():
    ash = Trainer("Ash")
    assert ash.get_team_size() == 0

def test_get_first_available():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    assert ash.get_first_available() == 'Charmander'
    
def test_get_first_available_skip():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 0, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Squirtel", 39, 12, 8, "Ember", 40, 0.2))
    assert ash.get_first_available() == 'Squirtel'
    
def test_get_first_available_None():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 0, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(FireType("Squirtel", 0, 12, 8, "Ember", 40, 0.2))
    assert ash.get_first_available() == None
    
def test___str__():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 0, 12, 8, "Ember", 40, 0.2))
    assert ash.__str__() == "Ash has 1 Pokemons"
    