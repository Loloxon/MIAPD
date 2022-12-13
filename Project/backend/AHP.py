from typing import List, Tuple, Union

import numpy as np

from Project.resources.DataBase import DataBase


class AHP:
    def __init__(self, db: DataBase):
        self._db = db
        self._priority_vectors = dict()
        self._calculate_priority_vector()

    def _aggregate_matrices(self):
        matrices = self._db.matrices
        new_matrices = dict()
        for k, v in matrices.items():
            array = np.array(v)
            aggregated = np.prod(array, axis=0)
            aggregated = np.power(aggregated, 1. / len(v))
            new_matrices[k] = aggregated
        return new_matrices

    def _calculate_priority_vector(self):
        matrices = self._aggregate_matrices()
        for k, matrix in matrices.items():
            normalized = matrix / np.sum(matrix, axis=0)
            summed = np.sum(normalized, axis=1)
            self._priority_vectors[k] = summed / matrix.shape[0]

    def calculate_ranking(self) -> Tuple[List[str], np.array]:
        weights = np.zeros(len(self._db.countries))
        subcategories_map = self._db.subcategories_map
        countries = self._db.countries
        categories = self._db.categories
        for i, country in enumerate(countries):
            weight = 0
            for cat, subcategories in subcategories_map.items():
                if not subcategories:
                    weight += self._priority_vectors[cat][i]*self._priority_vectors['categories'][categories.index(cat)]
                    continue
                partial_weight = 0
                for j, sub in enumerate(subcategories):
                    partial_weight += self._priority_vectors[sub][i] * self._priority_vectors[cat][j]
                weight += partial_weight * self._priority_vectors['categories'][categories.index(cat)]
            weights[i] = weight
        country_ranking = [country for _, country in sorted(zip(weights, countries), reverse=True)]
        return country_ranking, sorted(weights, reverse=True)

    def get_inconsistency_index(self, matrix: str, expert: Union[int, str]) -> float:
        matrix = self._db.get_matrix(matrix, expert)

        # TODO check calculating inconsistency_index
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        max_eigenvalue = max(eigenvalues)
        index = (max_eigenvalue - matrix.shape[0]) / (matrix.shape[0] - 1)
        return index




