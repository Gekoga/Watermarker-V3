from PIL.ImageQt import ImageQt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import (
    QPixmap,
)
from PyQt6.QtCore import Qt

from observerPattern import Observer, Subject
from CustomPyQtElements.fileSelector import FileNameSubject
from imageHelper import ImageHelper


class ReactiveImageField(Observer):
    image_helper = ImageHelper()
    _image_container: QLabel

    def __init__(self) -> None:
        super().__init__()
        self._image_container = QLabel("Hier komt een afbeelding")

    def update(self, subject: Subject) -> None:
        if type(subject) != FileNameSubject:
            return

        try:
            pixmap = QPixmap.fromImage(
                ImageQt(self.image_helper.getImageFromPath(subject.getFileName()))
            )
            scaled_pixmap = pixmap.scaledToWidth(
                300, Qt.TransformationMode.SmoothTransformation
            )
            self._image_container.setPixmap(scaled_pixmap)
        except Exception as e:
            print("Error: Pixmap preview")
            print(f"{e}")

        return super().update(subject)

    def getImageLabel(self) -> QLabel:
        return self._image_container
