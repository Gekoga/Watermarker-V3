import sys
from PyQt6.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout
from CustomPyQtElements.valueSlider import CustomSlider
from CustomPyQtElements.watermarkTextField import CustomWatermarkInput
from CustomPyQtElements.imageContainer import ReactiveImageField
from CustomPyQtElements.imageContainer import ReactiveImageOverlay
from CustomPyQtElements.fileSelector import CustomFileSelector
from CustomPyQtElements.inputField import ReactiveCustomInput


class Window(QWidget):
    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Watermarker V3")

        left_layout = QVBoxLayout()
        # File selector
        file_selector = CustomFileSelector(CustomFileSelector.FileTypes.IMAGES)
        left_layout.addWidget(file_selector)

        # Watermark text
        watermark_input = CustomWatermarkInput()
        left_layout.addWidget(watermark_input)

        # Marked image name
        marked_image_input = ReactiveCustomInput("Image name")
        file_selector._file_name_subject.attach(marked_image_input)

        left_layout.addWidget(marked_image_input.getInputField())

        right_layout = QVBoxLayout()
        preview_layout = QGridLayout()
        # Preview image
        preview_image = ReactiveImageField()
        file_selector._file_name_subject.attach(preview_image)

        preview_layout.addWidget(preview_image.getImageLabel(), 0, 0)

        # Preview watermark text
        preview_watermark = ReactiveImageOverlay()
        watermark_input._watermark_text_subject.attach(preview_watermark) # Attach watermark overlay to changes to the watermark input
        file_selector._file_name_subject.attach(preview_watermark) # Attach watermark overlay to changes to the selected image

        preview_layout.addWidget(preview_watermark.getOverlayLabel(), 0, 0)

        right_layout.addLayout(preview_layout)

        # Font size
        font_slider = CustomSlider("Font size", 1)
        right_layout.addWidget(font_slider)
        font_slider._number_subject.attach(preview_watermark) # Attach watermark overlay to changes in font size

        # Font alpha
        alpha_slider = CustomSlider("Alpha value", 1, 255, 150)
        right_layout.addWidget(alpha_slider)
        alpha_slider._number_subject.attach(preview_watermark) # Attach watermark overlay to changes in font alpha (see-through)


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
