from point_cloud_utils import *
from view import View
from qt_material import apply_stylesheet
from PySide2.QtWidgets import QApplication
import os.path as osp

class Controller():
    def __init__(self) -> None:
        self.app = QApplication([])
        self.view = View()
        self.index = 0

        self.signal_connect()

    def run(self):
        apply_stylesheet(self.app, theme='dark_teal.xml')
        self.view.show()
        self.app.exec_()


    def signal_connect(self):
        self.view.ui.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        curr_bin_path = osp.join("data/point_cloud", str(self.index).zfill(6) + ".bin")
        print(curr_bin_path)
        curr_points = read_bin(curr_bin_path)[0]
        print(curr_points.shape)
        self.view.set_point_cloud(curr_points)

        self.index += 1




if __name__=="__main__":
    obj = Controller()
    obj.run()