from copy import deepcopy
from typing import Dict, List, Union, Tuple
import numpy as np

# Kolejność robienia rzeczy
# 1. Załadowanie nazw kategorii, krajów i ekspertów z pliku
# 2. Ewentualne dodanie nowych danych przez użytkownika i usunięcie starych
# 3. Wygenerowanie macierzy i wpisanie do nich danych

class DataBase:
    def __init__(self):
        # TODO add loading from file
        self._subcategories_map: Dict[str, List[str]] = dict()
        self._matrices: Dict[str, List[np.array]] = dict()
        self._experts_map = dict()
        self._countries_map = dict()
        self._categories_map = dict()

    def add_expert(self, name: str) -> None:
        self._experts_map[name] = len(self._experts_map)

    def add_country(self, name: str) -> None:
        self._countries_map[name] = len(self._countries_map)

    def generate_matrices(self) -> None:
        new_matrices = dict()
        for k, v in self._subcategories_map.items():
            if not v:
                new_matrices[k] = [np.identity(len(self._countries_map), dtype=np.float64) for _ in range(len(self._experts_map))]
                continue
            new_matrices[k] = [np.identity(len(v), dtype=np.float64) for _ in range(len(self._experts_map))]
            for sub in v:
                new_matrices[sub] = [np.identity(len(self._countries_map), dtype=np.float64) for _ in range(len(self._experts_map))]
        number_of_categories = len(self._subcategories_map.keys())
        new_matrices['categories'] = [np.identity(number_of_categories, dtype=np.float64) for _ in range(len(self._experts_map))]
        self._matrices = new_matrices

    def add_category(self, category: str) -> None:
        self._subcategories_map[category] = []
        self._categories_map[category] = len(self._categories_map)

    def add_subcategory(self, category: str, subcategory: str) -> None:
        if category not in self._subcategories_map.keys():
            self._subcategories_map[category] = []
            self._categories_map[category] = len(self._categories_map)
        self._subcategories_map[category].append(subcategory)

    def get_matrix(self, name: str, expert: Union[int, str]) -> np.array:
        if isinstance(expert, str):
            expert = self._experts_map[expert]
        # for weight of categories use name 'categories'
        return deepcopy(self._matrices[name][expert])

    def set_matrix_field(self, name: str, expert: Union[int, str], i: int, j: int, value: float) -> None:
        if isinstance(expert, str):
            expert = self._experts_map[expert]
        self._matrices[name][expert][i][j] = value

# not used anymore
    # def set_matrix(self, name: str, expert: Union[int, str], matrix: np.array) -> None:
    #     if isinstance(expert, str):
    #         expert = self._experts_map[expert]
    #     # for weight of categories use name 'categories'
    #     self._matrices[name][expert] = matrix

    def is_missing_data(self) -> List[Tuple[str, int]]:
        # return list of tuples with matrix name and expert index
        missing_matrices = []
        for k, v in self._matrices.items():
            for i, matrix in enumerate(v):
                if (matrix <= 0).any():
                    missing_matrices.append((k, i))
        return missing_matrices

    @property
    def matrices(self) -> Dict[str, List[np.array]]:
        return deepcopy(self._matrices)

    @property
    def experts_map(self) -> Dict[str, List[str]]:
        return deepcopy(self._experts_map)

    @property
    def subcategories_map(self) -> Dict[str, List[str]]:
        return deepcopy(self._subcategories_map)

    @property
    def countries_map(self) -> Dict[str, int]:
        return deepcopy(self._countries_map)

    @property
    def categories_map(self) -> Dict[str, int]:
        return deepcopy(self._categories_map)
