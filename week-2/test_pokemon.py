from pokemon import WaterType, Pokemon, FireType

def test_get_current_hp():
    pikachu = Pokemon("Pikachu", 35, 11, 7, "Quick Attack", 10)
    assert pikachu.current_hp == 35

def test_is_fainted_True():
    pikachu = Pokemon("Pikachu", 0, 11, 7, "Quick Attack", 10)
    assert pikachu.is_fainted() == True

def test_is_fainted_False():
    pikachu = Pokemon("Pikachu", 1, 11, 7, "Quick Attack", 10)
    assert pikachu.is_fainted() == False

def test_attack_move():
    pikachu = Pokemon("Pikachu", 1, 11, 7, "Quick Attack", 10)
    assert pikachu.attack_move() == "Pikachu uses Quick Attack!"
    
def test__str__():
    pikachu = Pokemon("Pikachu", 1, 11, 7, "Quick Attack", 10)
    assert pikachu.__str__() == "Pikachu has 100.0 hp"
    
def test_FireTypedescription():
    pikachu = FireType("Pikachu", 1, 11, 7, "Quick Attack", 10, 0.2)
    assert pikachu.description() == "Pikachu is Fire Type with a burn chance 0.2%"
    
def test_WaterTypedescription():
    pikachu = WaterType("Pikachu", 1, 11, 7, "Quick Attack", 10, 5)
    assert pikachu.description() == "Pikachu is a Water Type with the swim speed 5"
    
def Pokemondescription():
    pikachu = Pokemon("Pikachu", 1, 11, 7, "Quick Attack", 10)
    assert pikachu.description() == "Pikachu is a Normal Type"