from sys import argv, exit
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from Interface import Ui_MainWindow
from Game import Game
from Database import Database


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('media/icon.png'))
        self.show()

        Database.connect()
        self.game = Game(
            self,
            self.widget,
            self.label__score,
            self.label__best,
            self.modal__lose
        )

        self.game.get_players()
        self.game.get_settings()
        self.game.get_snapshots()
        self.game.get_scores()
        if self.game.prepare_objects():
            self.game.start()

            self.mouse_slide_coord = []
            self.has_clicked_in_widget = False

            self.btn__restart.clicked.connect(self.game.restart)
            self.btn__undo.clicked.connect(self.game.undo)
            self.btn__change_user.clicked.connect(self.game.change_user)
            self.btn__table.clicked.connect(self.game.show_table)
        else:
            self.close()
            quit()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            self.mousePressEvent(event)
            return True
        if event.type() == QEvent.MouseButtonRelease:
            self.mouseReleaseEvent(event)
            return True
        return False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.game.move(0)
        elif event.key() == Qt.Key_Right:
            self.game.move(1)
        elif event.key() == Qt.Key_Up:
            self.game.move(2)
        elif event.key() == Qt.Key_Down:
            self.game.move(3)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            coord = [event.windowPos().x(), event.windowPos().y()]
            widget_x = self.widget.x()
            widget_y = self.widget.y()
            widget_end_x = widget_x + self.widget.width()
            widget_end_y = widget_y + self.widget.height()
            self.mouse_slide_coord = coord.copy()
            self.has_clicked_in_widget = widget_x <= coord[0] <= widget_end_x and widget_y <= coord[1] <= widget_end_y

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.has_clicked_in_widget:
            # По какой оси изменение больше, по той и двигаем
            delta_x = event.windowPos().x() - self.mouse_slide_coord[0]
            delta_y = event.windowPos().y() - self.mouse_slide_coord[1]
            abs_delta_x = abs(delta_x)
            abs_delta_y = abs(delta_y)
            if abs_delta_x > abs_delta_y:
                if delta_x > 0:
                    self.game.move(1)
                elif delta_x < 0:
                    self.game.move(0)
            elif abs_delta_y > abs_delta_x:
                if delta_y > 0:
                    self.game.move(3)
                elif delta_y < 0:
                    self.game.move(2)

    def closeEvent(self, event):
        self.game.save_players()
        self.game.save_settings()
        self.game.save_snapshots()
        self.game.save_scores()
        Database.close()


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    exit(app.exec())
