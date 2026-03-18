from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout

from imageHelper import ImageHelper
from observerPattern import Subject


class SaveEventSubject(Subject):
    _something: str

image_helper = ImageHelper()

class CustomSaveButton(QWidget):

    def __init__(self) -> None:
        super().__init__()

        # Save button
        # TODO: This activates a subject that needs to be observed
        save_button = QPushButton("Save")

        @save_button.clicked.connect
        def _():
            print("Save the image and export it to the computer!!")
            print(image_helper.getFontColor())

        layout = QHBoxLayout()
        layout.addWidget(save_button)

        self.setLayout(layout)
