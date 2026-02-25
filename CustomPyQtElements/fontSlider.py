from CustomPyQtElements.BaseElements.valueSlider import CustomSlider, NumberSubject


class FontSubject(NumberSubject):
    def getFontSize(self) -> int:
        return super().getSliderValue()


class CustomFontSlider(CustomSlider):
    def __init__(
        self,
        minimum: int = 0,
        maximum: int = 100,
        starting_value: int = 50,
    ) -> None:
        super().__init__("Font size", minimum, maximum, starting_value)

        self._number_subject = FontSubject()
        self._number_subject.updateSliderValue(starting_value)
