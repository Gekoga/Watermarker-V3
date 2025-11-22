from PyQt6.QtWidgets import QLabel, QWidget, QLineEdit, QVBoxLayout
from observerPattern import Subject, Observer
from CustomPyQtElements.fileSelector import FileNameSubject


class CustomInputField(QWidget):
    def __init__(self, informing_text) -> None:
        super().__init__()

        informing_label = QLabel(f"{informing_text}")

        self.input_field = QLineEdit()
        self.input_field.setEnabled(True)

        layout = QVBoxLayout()
        layout.addWidget(informing_label)
        layout.addWidget(self.input_field)

        self.setLayout(layout)

    def updateInputField(self, new_input_text):
        self.input_field.setText(new_input_text)


class ReactiveCustomInput(Observer):
    _input_field: CustomInputField

    def __init__(self, informing_text) -> None:
        super().__init__()
        self._input_field = CustomInputField(informing_text)

    def update(self, subject: Subject) -> None:

        # TODO: if there are multiple different subjects, change it to a switch statement, with functions
        if type(subject) != FileNameSubject:
            return

        self._input_field.updateInputField(subject.getFileName())
        print("Update the input field")

    def getInputField(self) -> CustomInputField:
        return self._input_field