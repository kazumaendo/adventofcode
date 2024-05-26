from dataclasses import dataclass
import re
from typing import Dict, Tuple
from models.custom_exceptions import ExtractionError

@dataclass
class City():
    def __init__(self, name: str) -> None:
        self.name = name
        self.path_to_another_city: Dict[City, int] = {}

    def __hash__(self):
        return hash(self.name)
    
    def __repr__(self):
        return f"City name: {self.name},\nlinks:\n"+('\n'.join([f"{city.name}: {distance}" for city, distance in self.path_to_another_city.items()]))
    
    def add_distance_to_another_city(self, city: 'City', distance: int) -> None:
        self.path_to_another_city[city] = distance

class CityNetworkBuilder():
    def __init__(self) -> None:
        self.seen_cities: Dict[str, City] = {}
    
    def process_city(self, input_str: str):
        try:
            from_city_name, to_city_name, distance = self.extract_input_string(input_str)
        except ExtractionError as e:
            print(e)

        if from_city_name not in self.seen_cities:
            self.create_city(from_city_name)
        if to_city_name not in self.seen_cities:
            self.create_city(to_city_name)
        
        from_city = self.get_city(from_city_name)
        to_city = self.get_city(to_city_name)
        self.update_city(from_city, to_city, distance)

    def create_city(self, city_name: str):
        city = City(city_name)
        self.seen_cities[city_name] = city

    def update_city(self, from_city: City, to_city: City, distance: int):
        from_city.add_distance_to_another_city(to_city, distance)
        to_city.add_distance_to_another_city(from_city,distance)

    def get_city(self, city_name: str):
        return self.seen_cities[city_name]
    
    def extract_input_string(self, input_str: str) -> Tuple[str,str,int]:
        input_pattern = r'([a-zA-Z\s]+) to ([a-zA-Z\s]+) = (\d+)'
        matches = re.match(input_pattern, input_str)

        if matches:
            try:
                from_city_name = matches.group(1).strip()
                to_city_name = matches.group(2).strip()
                distance = int(matches.group(3))
            except(IndexError, ValueError):
                raise ExtractionError(f"Input string: \"{input_str}\" is not in the right format")
            return from_city_name, to_city_name, distance
        else:
            raise ExtractionError(f"Input string: \"{input_str}\" is not in the right format")
