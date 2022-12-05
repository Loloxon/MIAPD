from typing import List, Tuple

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
        weights = np.zeros(len(self._db.countries_map))
        subcategories_map = self._db.subcategories_map
        countries = self._db.countries_map
        categories = self._db.categories_map
        for country, i in countries.items():
            weight = 0
            for cat, subcategories in subcategories_map.items():
                if not subcategories:
                    weight += self._priority_vectors[cat][i]*self._priority_vectors['categories'][categories[cat]]
                    continue
                partial_weight = 0
                for j, sub in enumerate(subcategories):
                    partial_weight += self._priority_vectors[sub][i] * self._priority_vectors[cat][j]
                weight += partial_weight * self._priority_vectors['categories'][categories[cat]]
            weights[i] = weight
        country_ranking = sorted(countries.keys(), key=lambda x: weights[countries[x]], reverse=True)
        return country_ranking, sorted(weights, reverse=True)



