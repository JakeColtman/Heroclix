import json
from Game.Engine.Map.Map import Map

class MapRepository:

    def __init__(self):
        self.maps = []

    def save_map(self, details):
        with open("../Map/Info/{0}.json".format(details["name"]), "w") as map_file:
            json.dump(details, map_file)

    def get_map_by_id(self, id):
        with open("../Map/Info/{0}.json".format("example"), "r") as map_file:
            json_map = json.load(map_file)

        map = Map(json_map["width"], json_map["height"])
        map.blocking = json_map["blocking"]