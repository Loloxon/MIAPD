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
        self._experts = []
        self._countries = []
        self._categories = []
        self.generate_matrices()  # TODO replace with loading from file

    def add_expert(self, name: str) -> None:
        self._experts.append(name)
        for category, matrices in self._matrices.items():
            matrices.append(np.identity(len(self._countries), dtype=np.float64))

    def add_country(self, name: str) -> None:
        self._countries.append(name)
        for category, subcategories in self._subcategories_map.items():
            if not subcategories:
                for matrix in self._matrices[category]:
                    matrix = np.insert(matrix, len(self._countries) - 1, 0, axis=0)
                    matrix = np.insert(matrix, len(self._countries) - 1, 0, axis=1)
                    matrix[-1][-1] = 1
            else:
                for subcategory in subcategories:
                    for matrix in self._matrices[subcategory]:
                        matrix = np.insert(matrix, len(self._countries) - 1, 0, axis=0)
                        matrix = np.insert(matrix, len(self._countries) - 1, 0, axis=1)
                        matrix[-1][-1] = 1

    def generate_matrices(self) -> None:
        new_matrices = dict()
        for k, v in self._subcategories_map.items():
            if not v:
                new_matrices[k] = [np.identity(len(self._countries), dtype=np.float64) for _ in range(len(self._experts))]
                continue
            new_matrices[k] = [np.identity(len(v), dtype=np.float64) for _ in range(len(self._experts))]
            for sub in v:
                new_matrices[sub] = [np.identity(len(self._countries), dtype=np.float64) for _ in range(len(self._experts))]
        number_of_categories = len(self._subcategories_map.keys())
        new_matrices['categories'] = [np.identity(number_of_categories, dtype=np.float64) for _ in range(len(self._experts))]
        self._matrices = new_matrices

    def add_category(self, category: str) -> None:
        self._subcategories_map[category] = []
        self._categories.append(category)
        for matrix in self._matrices['categories']:
            matrix = np.insert(matrix, len(self._categories) - 1, 0, axis=0)
            matrix = np.insert(matrix, len(self._categories) - 1, 0, axis=1)
            matrix[-1][-1] = 1
        self._matrices[category] = [np.identity(len(self._countries), dtype=np.float64) for _ in range(len(self._experts))]

    def add_subcategory(self, category: str, subcategory: str) -> None:
        if category not in self._subcategories_map.keys():
            self.add_category(category)
        self._subcategories_map[category].append(subcategory)
        if len(self._subcategories_map[category]) == 1: # if it's the first subcategory we need to make new matrix
            for matrix in self._matrices[category]:
                matrix = np.identity(1)
        else:
            for matrix in self._matrices[category]:
                matrix = np.insert(matrix, len(self._subcategories_map[category]) - 1, 0, axis=0)
                matrix = np.insert(matrix, len(self._subcategories_map[category]) - 1, 0, axis=1)
                matrix[-1][-1] = 1

    def get_matrix(self, name: str, expert: Union[int, str]) -> np.array:
        if isinstance(expert, str):
            expert = self._experts.index(expert)
        # for weight of categories use name 'categories'
        return deepcopy(self._matrices[name][expert])

    def set_matrix_field(self, name: str, expert: Union[int, str], i: Union[int, str], j: Union[int, str], value: float) -> None:
        if isinstance(expert, str):
            expert = self._experts.index(expert)
        if isinstance(i, str):
            if name in self._subcategories_map.keys():
                i = self._subcategories_map[name].index(i)
            else:
                i = self._countries.index(i)
        if isinstance(j, str):
            if name in self._subcategories_map.keys():
                j = self._subcategories_map[name].index(j)
            else:
                j = self._countries.index(j)
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
    def experts(self) -> List[str]:
        return deepcopy(self._experts)

    @property
    def subcategories_map(self) -> Dict[str, List[str]]:
        return deepcopy(self._subcategories_map)

    @property
    def countries(self) -> List[str]:
        return deepcopy(self._countries)

    @property
    def categories(self) -> List[str]:
        return deepcopy(self._categories)
