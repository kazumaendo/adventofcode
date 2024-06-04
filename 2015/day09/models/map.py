import heapq
import itertools
import logging
from typing import Set, Tuple
from models.cities import City, CityNetworkBuilder

class Map():
    # map_file requires absolute path to the file
    def __init__(self, map_file) -> None:
        city_map = CityNetworkBuilder()
        with open(map_file) as f:
            for line in f:
                city_map.process_city(line)
        self.city_nodes = city_map.seen_cities
        self.all_city_names = list(city_map.seen_cities.keys())
        self.city_count = len(self.all_city_names)
    
    def find_shortest_distance_to_cover_all_cities(self):
        distances_for_each_path = []
        for path in self.all_city_paths():
            distances_for_each_path.append(self.distance_for_path(path))
        return min(distance for distance in distances_for_each_path if distance is not None)

    def all_city_paths(self):
        permutations = list(itertools.permutations(self.all_city_names))
        return [list(permutation) for permutation in permutations]

    def distance_for_path(self, path: list) -> int:
        distance = 0
        starting_city_name = path[0]
        current_city = self.city_nodes.get(starting_city_name)
        for city in path[1:]:
            one_hop_distance = current_city.path_to_another_city.get(city)
            if one_hop_distance:
                distance+=current_city.path_to_another_city.get(city)
            else:
                return None
            current_city = self.city_nodes.get(city)
        return distance
