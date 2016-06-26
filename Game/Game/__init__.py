from Game.Engine.GameState import GameState
from Game.Engine.Character.Repository import CharacterRepository
from Game.Engine.Units.UnitFactory import UnitFactory
from Game.Engine.GameRepository import GameRepository

character_repo = CharacterRepository()
game_repo = GameRepository()

character_factory = UnitFactory(character_repo)

game_state = GameState()