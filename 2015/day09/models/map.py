import heapq
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
        self.city_verticies = list(city_map.seen_cities.values())
        self.city_count = len(self.city_verticies)
    
    def find_shortest_distance_to_cover_all_cities(self):
        distance_from_each_city = [self.find_shortest_distance_from_a_city(city) for city in self.city_verticies]
        print(f"kasdhfl: {distance_from_each_city}")
        return min(path for path in distance_from_each_city if distance_from_each_city is not None)


    # This algorithm is wrong. Revisit
    def find_shortest_distance_from_a_city(self, starting_city: City):
        # TODO: go through all cities and find shortest path using Djikstra algorithm.
        # Throws  None if the path does not exist from starting_city? 
        priority_queue = []
        # contains the cities leading up to the target city
        visited = {key.name: {key.name} for key in self.city_verticies}
        heapq.heappush(priority_queue, (0,starting_city))
        distances = {key.name: None for key in self.city_verticies}
        distances[starting_city.name] = 0
        print("--------------------------------------------")
        # print(f"For city: {starting_city.name}")
        
        flag = True
        while flag:
            _, city = heapq.heappop(priority_queue)
            # print(f"city-name: {city.name}")
            for adj_city, distance in city.path_to_another_city.items():
                adj_city_name = adj_city.name
                # if len(visited.get(adj_city_name)) > self.city_count:
                #     flag = False
                # print(f"adj-city-name: {adj_city_name}, distance: {distance}")
                if adj_city_name==city.name:
                    pass
                if distances[adj_city_name] == None or city.name not in visited[adj_city_name] or distances[adj_city_name] > (distances[city.name] + distance):
                    distances[adj_city_name] = distances[city.name] + distance
                    visited[adj_city_name].add(city.name)
                    # print(f"Interim visited: {visited[adj_city_name]}")
                    # print(f"Interim distance: {distances[city.name] + distance}")
                    heapq.heappush(priority_queue, (distances[adj_city_name], adj_city))
                # else:
                #     flag = False
        
        print(f"From city {starting_city.name}")
        for k,v in distances.items():
            print(f"{k}: {v}")
        
        distances_that_cover_all_cities = []
        for c, v_c in visited.items():
            print(f"asdf city: {c}")
            print(f"asdf visited cities: {v_c}")
            if len(v_c) == self.city_count:
                distances_that_cover_all_cities.append(distances[c])
        return None if not distances_that_cover_all_cities else min(distances_that_cover_all_cities)
        # return max(distances.values())
