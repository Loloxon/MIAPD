from copy import deepcopy
from typing import Dict, List, Union
import numpy as np

# Kolejność robienia rzeczy
# 1. Załadowanie nazw kategorii, krajów i ekspertów z pliku
# 2. Ewentualne dodanie nowych danych przez użytkownika i usunięcie starych
# 3. Wygenerowanie macierzy i wpisanie do nich danych

class DataBase:
    def __init__(self):
        # TODO add loading from file
        self._subcategories_map: Dict[str: List[str]] = dict()
        self._matrices: Dict[str: List[np.array]] = dict()
        self._number_of_experts = 0
        self._number_of_countries = 0
        self._experts_map = dict()
        self._countries_map = dict()

    def add_expert(self, name: str) -> None:
        self._experts_map[self._number_of_experts] = name
        self._number_of_experts += 1

    def add_country(self, name: str) -> None:
        self._countries_map[self._number_of_countries] = name
        self._number_of_countries += 1

    def generate_matrices(self) -> None:
        new_matrices = dict()
        for k, v in self._subcategories_map.items():
            if not v:
                new_matrices[k] = np.identity(self._number_of_countries, dtype=np.float64)
                continue
            new_matrices[k] = np.identity(len(v), dtype=np.float64)
            for sub in v:
                new_matrices[sub] = np.identity(self._number_of_countries, dtype=np.float64)
        number_of_categories = len(self._subcategories_map.keys())
        new_matrices['categories'] = np.identity(number_of_categories, dtype=np.float64)
        self._matrices = new_matrices

    def add_category(self, category: str) -> None:
        self._subcategories_map[category] = []

    def add_subcategory(self, category: str, subcategory: str) -> None:
        if category not in self._subcategories_map.keys():
            self._subcategories_map[category] = []
        self._subcategories_map[category].append(subcategory)

    def get_matrix(self, name: str, expert: Union[int, str]) -> np.array:
        if isinstance(expert, str):
            expert = self._experts_map[expert]
        # for weight of categories use name 'categories'
        return self._matrices[name][expert]

    def is_missing_data(self) -> bool:
        # possibility to add returning what is missing
        for k, v in self._matrices.items():
            for matrix in v:
                if (matrix <= 0).any():
                    return True
        return False

    @property
    def matrices(self) -> Dict[str: List[np.array]]:
        return deepcopy(self._matrices)
