from __future__ import annotations

import pickle
from copy import deepcopy
from typing import Dict, List, Union, Tuple
import numpy as np


# Kolejność robienia rzeczy
# 1. Załadowanie nazw kategorii, krajów i ekspertów z pliku
# 2. Ewentualne dodanie nowych danych przez użytkownika i usunięcie starych
# 3. Wygenerowanie macierzy i wpisanie do nich danych

class DataBase:
    def __init__(self):
        self._subcategories_map: Dict[str, List[str]] = dict()
        self._matrices: Dict[str, List[np.array]] = dict()
        self._experts = []
        self._countries = []
        self._categories = []
        self._generate_matrices()

    def add_expert(self, name: str) -> None:
        self._experts.append(name)
        for category, matrices in self._matrices.items():
            matrices.append(np.identity(len(self._countries), dtype=np.float64))

    def add_country(self, name: str) -> None:
        self._countries.append(name)
        for category, subcategories in self._subcategories_map.items():
            if not subcategories:
                for i, matrix in enumerate(self._matrices[category]):
                    self._matrices[category][i] = add_row_col(matrix)
            else:
                for subcategory in subcategories:
                    for i, matrix in enumerate(self._matrices[subcategory]):
                        self._matrices[subcategory][i] = add_row_col(matrix)

    def _generate_matrices(self) -> None:
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
        for i, matrix in enumerate(self._matrices['categories']):
            self._matrices['categories'][i] = add_row_col(matrix)
        self._matrices[category] = [np.identity(len(self._countries), dtype=np.float64) for _ in range(len(self._experts))]

    def add_subcategory(self, category: str, subcategory: str) -> None:
        if category not in self._subcategories_map.keys():
            self.add_category(category)
        self._subcategories_map[category].append(subcategory)
        if len(self._subcategories_map[category]) == 1: # if it's the first subcategory we need to make new matrix
            self._matrices[category] = [np.identity(1, dtype=np.float64) for _ in range(len(self._experts))]
        else:
            for i, matrix in enumerate(self._matrices[category]):
                self._matrices[category][i] = add_row_col(matrix)

        self._matrices[subcategory] = [np.identity(len(self._countries), dtype=np.float64) for _ in range(len(self._experts))]

    def remove_expert(self, name: str) -> None:
        for category, matrices in self._matrices.items():
            matrices.pop(self._experts.index(name))
        self._experts.remove(name)

    def remove_country(self, name: str) -> None:
        for category, subcategories in self._subcategories_map.items():
            if not subcategories:
                for i, matrix in enumerate(self._matrices[category]):
                    self._matrices[category][i] = remove_row_col(matrix, self._countries.index(name))
            else:
                for subcategory in subcategories:
                    for i, matrix in enumerate(self._matrices[subcategory]):
                        self._matrices[subcategory][i] = remove_row_col(matrix, self._countries.index(name))
        self._countries.remove(name)

    def remove_category(self, name: str) -> None:
        # removes category and all subcategories associated with it
        for i, matrix in enumerate(self._matrices['categories']):
            self._matrices['categories'][i] = remove_row_col(matrix, self._categories.index(name))
        for subcategory in self._subcategories_map[name]:
            self._matrices.pop(subcategory)
        self._matrices.pop(name)
        self._categories.remove(name)
        self._subcategories_map.pop(name)

    def remove_subcategory(self, category: str, subcategory: str) -> None:
        for i, matrix in enumerate(self._matrices[category]):
            self._matrices[category][i] = remove_row_col(matrix, self._subcategories_map[category].index(subcategory))
        self._matrices.pop(subcategory)
        self._subcategories_map[category].remove(subcategory)

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
        self._matrices[name][expert][j][i] = max(min(1/value, 9), 1/9)

# not used anymore
    # def set_matrix(self, name: str, expert: Union[int, str], matrix: np.array) -> None:
    #     if isinstance(expert, str):
    #         expert = self._experts_map[expert]
    #     # for weight of categories use name 'categories'
    #     self._matrices[name][expert] = matrix

    def is_missing_data(self) -> List[Tuple[str, List[str]]]:
        # return list of tuples with matrix name and expert index
        missing_matrices = []
        for i in range(len(self._experts)):
            missing_for_expert = []
            for k, v in self._matrices.items():
                if (v[i] <= 0).any():
                    missing_for_expert.append(k)
            if missing_for_expert:
                missing_matrices.append((self._experts[i], missing_for_expert))
        return missing_matrices

    def save(self, path: str = 'DataBase.pkl') -> None:
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, path: str = 'DataBase.pkl') -> DataBase:
        with open(path, 'rb') as f:
            return pickle.load(f)

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


def add_row_col(matrix: np.array) -> np.array:
    matrix = np.insert(matrix, matrix.shape[0], 0, axis=0)
    matrix = np.insert(matrix, matrix.shape[1], 0, axis=1)
    matrix[-1][-1] = 1
    return matrix


def remove_row_col(matrix: np.array, index: int) -> np.array:
    matrix = np.delete(matrix, index, axis=0)
    matrix = np.delete(matrix, index, axis=1)
    return matrix
