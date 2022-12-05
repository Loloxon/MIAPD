import numpy as np

from Project.resources.DataBase import DataBase


class AHP:
    def __init__(self, db: DataBase):
        self._db = db
        self._priority_vectors = dict()

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

    def calculate_ranking(self):
        # TODO
        pass

