from PyQt6.QtWidgets import QLabel, QWidget, QLineEdit, QVBoxLayout
from CustomSubjects.colorSubject import ColorSubject
from observerPattern import Subject, Observer
from CustomPyQtElements.BaseElements.fileSelector import FileNameSubject


class CustomInputField(QWidget):
    def __init__(self, informing_text="") -> None:
        super().__init__()

        layout = QVBoxLayout()

        # If informing_text is spaces or empty, don't add it
        if not informing_text.isspace() and informing_text:
            informing_label = QLabel(f"{informing_text}")
            layout.addWidget(informing_label)

        self.input_field = QLineEdit()
        self.input_field.setEnabled(True)
        layout.addWidget(self.input_field)

        self.setLayout(layout)

    def updateInputField(self, new_input_text):
        self.input_field.setText(new_input_text)


class ReactiveCustomInput(Observer):
    _input_field: CustomInputField

    def __init__(self, informing_text="") -> None:
        super().__init__()
        self._input_field = CustomInputField(informing_text)

    def update(self, subject: Subject) -> None:
        match subject:
            case FileNameSubject():
                self._input_field.updateInputField(subject.getFileName())
            case ColorSubject():
                self._input_field.updateInputField(subject.getColorString())

    def getInputField(self) -> CustomInputField:
        return self._input_field
