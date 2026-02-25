from CustomPyQtElements.BaseElements.valueSlider import CustomSlider, NumberSubject


class AlphaSubject(NumberSubject):
    def getAlphaValue(self) -> int:
        return super().getSliderValue()


class CustomAlphaSlider(CustomSlider):
    def __init__(
        self,
        minimum: int = 0,
        maximum: int = 255,
        starting_value: int = 150,
    ) -> None:
        super().__init__("Alpha value", minimum, maximum, starting_value)

        self._number_subject = AlphaSubject()
        self._number_subject.updateSliderValue(starting_value)
