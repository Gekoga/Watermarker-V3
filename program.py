import sys
from PyQt6.QtWidgets import (
    QPushButton,
    QWidget,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
)
from CustomPyQtElements.alphaSlider import CustomAlphaSlider
from CustomPyQtElements.colorPicker import CustomColorPicker
from CustomPyQtElements.saveButton import CustomSaveButton
from CustomPyQtElements.fontSlider import CustomFontSlider
from CustomPyQtElements.watermarkTextField import CustomWatermarkInput
from CustomPyQtElements.imageContainer import ReactiveImageField
from CustomPyQtElements.imageContainer import ReactiveImageOverlay
from CustomPyQtElements.BaseElements.fileSelector import CustomFileSelector
from CustomPyQtElements.BaseElements.inputField import ReactiveCustomInput

# TODO: Check for beter looks with QtSS (Qt Style Sheets)


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
        # Attach watermark overlay to changes to the watermark input
        watermark_input._watermark_text_subject.attach(preview_watermark)
        file_selector._file_name_subject.attach(preview_watermark)

        preview_layout.addWidget(preview_watermark.getOverlayLabel(), 0, 0)

        right_layout.addLayout(preview_layout)

        # Font size
        font_slider = CustomFontSlider(minimum=1)
        right_layout.addWidget(font_slider)
        # Attach watermark overlay to changes in font size & Update after initialisation, because of the default values
        font_slider._number_subject.attach(preview_watermark)
        font_slider._number_subject.notifySingleObserver(preview_watermark)

        # Font alpha
        alpha_slider = CustomAlphaSlider()
        right_layout.addWidget(alpha_slider)
        # Attach watermark overlay to changes in font alpha (see-through) & Update after initialisation, because of the default values
        alpha_slider._number_subject.attach(preview_watermark)
        alpha_slider._number_subject.notifySingleObserver(preview_watermark)

        # Font colour
        color_picker = CustomColorPicker()
        right_layout.addWidget(color_picker)
        # Attach watermark overlay to changes in font color & Update after initialisation, because of the default values
        color_picker._color_subject.attach(preview_watermark)


        buttons_layout = QHBoxLayout()

        # Save/Export buttons
        save_button = CustomSaveButton()

        # Cancel button
        cancel_button = QPushButton("Cancel")
        @cancel_button.clicked.connect
        def _():
            sys.exit(0)

        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(cancel_button)

        right_layout.addLayout(buttons_layout)

        application_layout = QHBoxLayout()
        application_layout.addLayout(left_layout)
        application_layout.addLayout(right_layout)
        self.setLayout(application_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(None)
    window.show()
    sys.exit(app.exec())
