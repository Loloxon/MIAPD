from Project.resources.DataBase import DataBase
from Project.backend.AHP import AHP
import numpy as np

if __name__ == '__main__':
    db = DataBase()
    db.add_expert('expert1')
    db.add_country('country1')
    db.add_country('country2')
    db.add_country('country3')
    db.add_country('country4')

    db.add_category('cost')
    db.add_subcategory('cost', 'purchase')
    db.add_subcategory('cost', 'fuel')
    db.add_subcategory('cost', 'maintenance')
    db.add_category('safety')
    db.add_category('design')
    db.add_subcategory('capacity', 'trunk')
    db.add_subcategory('capacity', 'passenger')
    db.add_category('warranty')

    db.generate_matrices()

    db.set_matrix('cost', 'expert1', np.array([[1, 7, 8], [1/7, 1, 3], [1/8, 1/3, 1]]))
    db.set_matrix('purchase', 'expert1', np.array([[1, 7/5, 4/9, 4/5], [5/7, 1, 6/7, 7/6], [9/4, 7/6, 1, 3/2], [5/4, 6/7, 2/3, 1]]))
    db.set_matrix('fuel', 'expert1', np.array([[1, 7/3, 9/5, 2], [3/7, 1, 8/5, 8/5], [5/9, 5/8, 1, 2], [1/2, 5/8, 1/2, 1]]))
    db.set_matrix('maintenance', 'expert1', np.array([[1, 7/5, 4/3, 5/9], [5/7, 1, 2, 6/5], [3/4, 1/2, 1, 3/2], [9/5, 5/6, 2/3, 1]]))

    db.set_matrix('safety', 'expert1', np.array([[1, 2/5, 1/9, 1/7], [2/5, 1, 1/9, 1/4], [9, 9, 1, 5], [7, 4, 1/5, 1]]))

    db.set_matrix('design', 'expert1', np.array([[1, 1/9, 1/9, 1/9], [9, 1, 5, 9/8], [9, 1/5, 1, 7/9], [9, 8/9, 9/7, 1]]))

    db.set_matrix('capacity', 'expert1', np.array([[1, 3], [1/3, 1]]))
    db.set_matrix('trunk', 'expert1', np.array([[1, 6/5, 2/3, 5/2], [5/6, 1, 5/9, 7/5], [3/2, 9/5, 1, 1], [2/5, 5/7, 1, 1]]))
    db.set_matrix('passenger', 'expert1', np.array([[1, 9, 9, 3/8], [1/9, 1, 2/3, 1/9], [1/9, 3/2, 1, 1/9], [8/3, 9, 9, 1]]))

    db.set_matrix('warranty', 'expert1', np.array([[1, 9, 4/3, 7/5], [1/9, 1, 1/9, 1/9], [3/4, 9, 1, 1/2], [5/7, 9, 2, 1]]))

    db.set_matrix('categories', 'expert1', np.array([[1, 7/5, 5, 9/5, 8], [5/7, 1, 9/5, 7/5, 5/4], [1/5, 5/9, 1, 3/7, 3/4], [5/9, 5/7, 7/3, 1, 7/9], [1/8, 4/5, 4/3, 9/7, 1]]))

    ahp = AHP(db)
    rank = ahp.calculate_ranking()
    print(rank)