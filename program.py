import sys
from PyQt6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout
from CustomPyQtElements.fileSelector import CustomFileSelector
from CustomPyQtElements.inputField import CustomInputField, ReactiveCustomInput


class Window(QWidget):
    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Watermarker V3")

        left_layout = QVBoxLayout()
        # File selector
        file_selector = CustomFileSelector(CustomFileSelector.FileTypes.IMAGES)
        left_layout.addWidget(file_selector)

        # Watermark text
        watermark_input = CustomInputField("Watermark text")
        left_layout.addWidget(watermark_input)

        # Marked image name
        marked_image_input = ReactiveCustomInput("Image name")
        file_selector._file_name_subject.attach(marked_image_input)

        left_layout.addWidget(marked_image_input.getInputField())

        right_layout = QVBoxLayout()
        # Preview image
        # Font size
        # Font alpha
        # Font colour
        # Save/Cancel buttons

        application_layout = QHBoxLayout()
        application_layout.addLayout(left_layout)
        application_layout.addLayout(right_layout)
        self.setLayout(application_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(None)
    window.show()
    sys.exit(app.exec())
