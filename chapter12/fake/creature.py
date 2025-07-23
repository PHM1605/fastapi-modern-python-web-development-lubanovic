from model.creature import Creature 
from error import Duplicate, Missing

_creatures = [
    Creature(name="Yeti", aka="Abominable Snowman", country="CN", area="Himalayas", description="Hirsute Himalayan"),
    Creature(name="Bigfoot", description="Yeti's Cousin Eddie", country="US", area="*", aka="Sasquatch")
]

def get_all() -> list[Creature]:
    return _creatures

def get_one(name:str)->Creature|None:
    for creature in _creatures:
        if creature.name == name:
            return creature 
    raise Missing(f"Creature '{name}' not found") None 

def create(creature:Creature) -> Creature:
    if any(c.name == creature.name for c in _creatures):
        raise Duplicate(f"Creature with name '{creature.name}' already exists.")
    _creatures.append(creature)
    return creature 

def modify(name:str, creature:Creature) -> Creature:
    for i, existing in enumerate(_creatures):
        if existing.name == name:
            _creatures[i] = creature 
            return creature 
    raise Missing(f"Creature '{name}' not found for modification")

def replace(name:str, creature:Creature)->Creature:
    for i, existing in enumerate(_creatures):
        if existing.name == name:
            _creatures[i] = creature 
            return creature 
    # if not found, create it (replace = upsert)
    _creatures.append(creature)
    return creature 

def delete(name: str):
    for i, creature in enumerate(_creatures):
        if creature.name == name:
            del _creatures[i]
            return 
    raise Missing(f"Creature '{name}' not found for deletion")
