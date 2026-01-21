from PIL.ImageQt import ImageQt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import (
    QPixmap,
)
from PyQt6.QtCore import Qt

from observerPattern import Observer, Subject
from CustomPyQtElements.fileSelector import FileNameSubject
from CustomPyQtElements.watermarkTextField import WatermarkTextSubject
from imageHelper import ImageHelper

image_helper = ImageHelper()


class ReactiveImageField(Observer):
    _image_container: QLabel

    def __init__(self) -> None:
        super().__init__()
        self._image_container = QLabel("Hier komt een afbeelding")

    def update(self, subject: Subject) -> None:
        if type(subject) != FileNameSubject:
            return

        try:
            pixmap = QPixmap.fromImage(
                ImageQt(image_helper.getImageFromPath(subject.getFileName()))
            )
            scaled_pixmap = pixmap.scaledToWidth(
                image_helper.TARGET_WIDTH, Qt.TransformationMode.SmoothTransformation
            )
            self._image_container.setPixmap(scaled_pixmap)
        except Exception as e:
            print("Error: Pixmap preview")
            print(f"{e}")

        return super().update(subject)

    def getImageLabel(self) -> QLabel:
        return self._image_container


class ReactiveImageOverlay(Observer):
    _overlay_container: QLabel

    def __init__(self) -> None:
        super().__init__()
        self._overlay_container = QLabel()

    def update(self, subject: Subject) -> None:
        # if type(subject) != WatermarkTextSubject:
        #     return
        
        try:
            overlay_image = image_helper.getCopyOfOverlay()
            self._overlay_container.setPixmap(QPixmap.fromImage(ImageQt(overlay_image)))
        except Exception as e:
            print("Error: overlay image")
            print(f"{e}")

        return super().update(subject)

    def getOverlayLabel(self) -> QLabel:
        return self._overlay_container
