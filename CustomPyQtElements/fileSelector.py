import enum
from observerPattern import Subject, Observer
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QFileDialog,
)


class FileNameSubject(Subject):
    _file_name: str

    def attach(self, observer: Observer) -> None:
        return super().attach(observer)

    def detach(self, observer: Observer) -> None:
        return super().detach(observer)

    def notify(self) -> None:
        return super().notify()

    def setFileName(self, file_name: str) -> None:
        self._file_name = file_name
        self.notify()

    def getFileName(self) -> str:
        return self._file_name


class CustomFileSelector(QWidget):
    class FileTypes(enum.Enum):
        ANY = ...
        IMAGES = ...
        TEXT = ...
        PDF = ...

    _file_name_subject: FileNameSubject

    def __init__(self, file_type: FileTypes) -> None:
        super().__init__()

        self._file_name_subject = FileNameSubject()

        informing_label = QLabel("Selected file")

        file_name_line = QLineEdit()
        file_name_line.setEnabled(False)
        file_name_line.setText("No file selected")

        select_file_button = QPushButton()
        select_file_button.setText("Select")

        # Decorator for button clicked, open the file dialog
        @select_file_button.clicked.connect
        def _():
            self.file_select_dialog.exec()

        self.file_select_dialog = QFileDialog()
        self.file_select_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        match file_type:
            case self.FileTypes.IMAGES:
                self.file_select_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
            case self.FileTypes.TEXT:
                self.file_select_dialog.setNameFilter("Text (*.txt)")
            case self.FileTypes.PDF:
                self.file_select_dialog.setNameFilter("PDF (*.pdf)")

        # Decorator for when a file is selected
        @self.file_select_dialog.fileSelected.connect
        def _(file_name: str):
            file_name_line.setText(file_name)
            self._file_name_subject.setFileName(file_name)

        action_layout = QHBoxLayout()
        action_layout.addWidget(file_name_line)
        action_layout.addWidget(select_file_button)

        layout = QVBoxLayout()
        layout.addWidget(informing_label)
        layout.addLayout(action_layout)

        self.setLayout(layout)
