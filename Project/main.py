from Project.gui.GUI import GUI
from Project.resources.DataBase import DataBase
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))

if __name__ == '__main__':
    db = DataBase()
    db = db.load()
    gui = GUI(db)
