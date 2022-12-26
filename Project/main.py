from Project.gui.GUI import GUI
from Project.resources.DataBase import DataBase


if __name__ == '__main__':
    db = DataBase()
    db = db.load()
    gui = GUI(db)
