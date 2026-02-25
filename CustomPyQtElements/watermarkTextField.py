from CustomPyQtElements.BaseElements.inputField import CustomInputField
from observerPattern import Subject


class WatermarkTextSubject(Subject):
    _watermark_text: str

    def setWatermarkText(self, watermark_text: str) -> None:
        self._watermark_text = watermark_text
        self.notify()

    def getWatermarkText(self) -> str:
        return self._watermark_text


class CustomWatermarkInput(CustomInputField):
    _watermark_text_subject: WatermarkTextSubject

    def __init__(self) -> None:
        super().__init__("Watermark text")

        self._watermark_text_subject = WatermarkTextSubject()

        # TODO: Check performance when using textChanged and editingFinished
        # textChanged -> each keypress
        # editingFinished -> when the user presses enter, or the field isn't in focus anymore

        # Decorator for when text in the input field is edited
        @self.input_field.textChanged.connect
        def _(input_text: str):
            self._watermark_text_subject.setWatermarkText(input_text)
