from PIL.ImageQt import ImageQt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import (
    QPixmap,
)
from PyQt6.QtCore import Qt

from CustomPyQtElements.valueSlider import NumberSubject
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
    _overlay_text: str

    def __init__(self) -> None:
        super().__init__()
        self._overlay_container = QLabel()
        self._overlay_text = ""

    def update(self, subject: Subject) -> None:
        match subject:
            case WatermarkTextSubject():
                self._overlay_text = subject.getWatermarkText()
            case FileNameSubject():
                print("FileNameSubject")
            case NumberSubject():
                # TODO: Make it that you can have multiple number subjects, not just the font size
                image_helper.setFontSize(subject.getSliderValue())

        try:
            # display the text once on the screen, the size of the font
            testing = image_helper.createTextOverlay(self._overlay_text)

            self._overlay_container.setPixmap(QPixmap.fromImage(ImageQt(testing)))
        except Exception as e:
            print("Error: overlay image")
            print(f"{e}")

        return super().update(subject)

    def getOverlayLabel(self) -> QLabel:
        return self._overlay_container
