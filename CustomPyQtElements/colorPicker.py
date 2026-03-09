# TODO: Create the base of this picker with an field for the hex code and small square with the color
# When you click on the square, a color dialog pops up (https://doc.qt.io/qt-6/qcolordialog.html)
# When you edit the hex code, the color changes for the small square and for the overlay color

from PyQt6.QtWidgets import QColorDialog, QHBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QColor
from CustomPyQtElements.BaseElements.inputField import ReactiveCustomInput
from CustomSubjects.colorSubject import ColorSubject


class CustomColorPicker(QWidget):
    _color_subject: ColorSubject

    def __init__(self) -> None:
        super().__init__()

        self._color_subject = ColorSubject()

        hex_field = ReactiveCustomInput("Select color")
        self._color_subject.attach(hex_field)

        # TODO: Change the styling of the button, so it is a square with the correct color
        select_color_button = QPushButton()
        select_color_button.setText("Pick color")

        @select_color_button.clicked.connect
        def _():
            self.color_dialog.exec()

        self.color_dialog = QColorDialog()

        @self.color_dialog.colorSelected.connect
        def _(selected_color: QColor):
            self._color_subject.setColor(selected_color)

        # TODO: Make this so you don't have to hardcode it here, but are able to call upon the needed object
        @hex_field._input_field.input_field.textChanged.connect
        def _(text: str):
            succeeded = self._color_subject.setColorFromString(text)

            if succeeded:
                self.color_dialog.setCurrentColor(QColor.fromString(text))

        color_layout = QHBoxLayout()
        color_layout.addWidget(hex_field.getInputField())
        color_layout.addWidget(select_color_button)

        self.setLayout(color_layout)
