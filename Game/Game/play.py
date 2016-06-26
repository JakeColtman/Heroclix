from Game.Engine.Character.Repository import CharacterRepository
from Game.Engine.Units.UnitFactory import UnitFactory

from Game.Engine.Player.Player import Player

from Game.Engine.Engine import Engine
from Game.Engine.Movement.Movement import Movement

repo = CharacterRepository()
unit = UnitFactory(repo)
BW = unit.create_character_by_id(1, [1,1])
BWEnemy = unit.create_character_by_id(1, [1,0])

jake_player = Player([BW])
opposing_players = Player([BWEnemy])

engine = Engine("Test", 10, [jake_player, opposing_players])

for move in [[1,2], [2,3]]:
    print(engine.movement(Movement(BW, move)))