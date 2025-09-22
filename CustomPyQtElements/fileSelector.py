import enum
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QFileDialog,
)


class CustomFileSelector(QWidget):
    class FileTypes(enum.Enum):
        ANY = ...
        IMAGES = ...
        TEXT = ...

    def __init__(self, file_type: FileTypes) -> None:
        super().__init__()

        informing_label = QLabel("Selected file")

        file_name_line = QLineEdit()
        file_name_line.setEnabled(False)
        file_name_line.setText("No file selected")

        select_file_button = QPushButton()
        select_file_button.setText("Select")

        @select_file_button.clicked.connect
        def _():
            file_select_dialog.exec()

        file_select_dialog = QFileDialog()
        file_select_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        match file_type:
            case self.FileTypes.IMAGES:
                file_select_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
            case self.FileTypes.TEXT:
                file_select_dialog.setNameFilter("Text (*.txt)")

        @file_select_dialog.fileSelected.connect
        def _(file_name):
            file_name_line.setText(f"{file_name}")

        action_layout = QHBoxLayout()
        action_layout.addWidget(file_name_line)
        action_layout.addWidget(select_file_button)

        layout = QVBoxLayout()
        layout.addWidget(informing_label)
        layout.addLayout(action_layout)

        self.setLayout(layout)
