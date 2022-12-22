import numpy as np

from Project.gui.GUI import GUI
from Project.resources.DataBase import DataBase


def init_data_base():
    db.add_expert('Bob, The Expert')
    db.add_country('USA')
    db.add_country('Russia')
    db.add_country('Germany')
    db.add_country('Japan')

    db.add_category('Army')
    db.add_subcategory('Army', 'Navy')
    db.add_subcategory('Army', 'Ground Forces')
    db.add_subcategory('Army', 'Air Forces')
    db.add_category('Distance')
    db.add_category('Potential Allies')
    db.add_category('Economy')
    db.add_subcategory('Economy', 'Current')
    db.add_subcategory('Economy', 'Predictions')
    db.add_category('Political Relationships')

    array = np.array([[1, 7, 8],
                      [1 / 7, 1, 3],
                      [1 / 8, 1 / 3, 1]])
    matrix = "Army"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array(
        [[1, 7 / 5, 4 / 9, 4 / 5],
         [5 / 7, 1, 6 / 7, 7 / 6],
         [9 / 4, 7 / 6, 1, 3 / 2],
         [5 / 4, 6 / 7, 2 / 3, 1]])
    matrix = "Navy"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 7 / 3, 9 / 5, 2],
                      [3 / 7, 1, 8 / 5, 8 / 5],
                      [5 / 9, 5 / 8, 1, 2],
                      [1 / 2, 5 / 8, 1 / 2, 1]])
    matrix = "Ground Forces"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array(
        [[1, 7 / 5, 4 / 3, 5 / 9],
         [5 / 7, 1, 2, 6 / 5],
         [3 / 4, 1 / 2, 1, 3 / 2],
         [9 / 5, 5 / 6, 2 / 3, 1]])
    matrix = "Air Forces"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 2 / 5, 1 / 9, 1 / 7],
                      [2 / 5, 1, 1 / 9, 1 / 4],
                      [9, 9, 1, 5],
                      [7, 4, 1 / 5, 1]])
    matrix = "Distance"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 1 / 9, 1 / 9, 1 / 9],
                      [9, 1, 5, 9 / 8],
                      [9, 1 / 5, 1, 7 / 9],
                      [9, 8 / 9, 9 / 7, 1]])
    matrix = "Potential Allies"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 3],
                      [1 / 3, 1]])
    matrix = "Economy"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array(
        [[1, 6 / 5, 2 / 3, 5 / 2],
         [5 / 6, 1, 5 / 9, 7 / 5],
         [3 / 2, 9 / 5, 1, 1],
         [2 / 5, 5 / 7, 1, 1]])
    matrix = "Current"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 9, 9, 3 / 8],
                      [1 / 9, 1, 2 / 3, 1 / 9],
                      [1 / 9, 3 / 2, 1, 1 / 9],
                      [8 / 3, 9, 9, 1]])
    matrix = "Predictions"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 9, 4 / 3, 7 / 5],
                      [1 / 9, 1, 1 / 9, 1 / 9],
                      [3 / 4, 9, 1, 1 / 2],
                      [5 / 7, 9, 2, 1]])
    matrix = "Political Relationships"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])

    array = np.array([[1, 7 / 5, 5, 9 / 5, 8],
                      [5 / 7, 1, 9 / 5, 7 / 5, 5 / 4],
                      [1 / 5, 5 / 9, 1, 3 / 7, 3 / 4],
                      [5 / 9, 5 / 7, 7 / 3, 1, 7 / 9],
                      [1 / 8, 4 / 5, 4 / 3, 9 / 7, 1]])
    matrix = "categories"
    expert = "Bob, The Expert"
    for i in range(len(array)):
        for j in range(len(array[0])):
            db.set_matrix_field(matrix, expert, i, j, array[i][j])


if __name__ == '__main__':
    db = DataBase()
    db = db.load()
    # init_data_base()
    gui = GUI(db)
