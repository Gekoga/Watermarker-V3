from observerPattern import Observer, Subject
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSlider
from PyQt6.QtCore import Qt

class NumberSubject(Subject):
    _slider_value: int

    def attach(self, observer: Observer) -> None:
        return super().attach(observer)

    def detach(self, observer: Observer) -> None:
        return super().detach(observer)

    def notify(self) -> None:
        return super().notify()

    def updateSliderValue(self, slider_value: int) -> None:
        self._slider_value = slider_value
        self.notify()

    def getSliderValue(self) -> int:
        return self._slider_value


class CustomSlider(QWidget):
    _number_subject: NumberSubject

    def __init__(
        self,
        slider_text: str,
        minimum: int = 0,
        maximum: int = 100,
        starting_value: int = 50,
    ) -> None:
        super().__init__()

        top_layout = QHBoxLayout()
        self._slider_label = QLabel(slider_text + ":")
        self._value_label = QLabel(f"{starting_value}")

        top_layout.addWidget(self._slider_label)
        top_layout.addWidget(self._value_label)

        bottom_layout = QHBoxLayout()
        self._minimum_label = QLabel(f"{minimum}")
        self._maximum_label = QLabel(f"{maximum}")

        self._value_slider = QSlider(Qt.Orientation.Horizontal)
        self._value_slider.setMinimum(minimum)
        self._value_slider.setMaximum(maximum)
        self._value_slider.setValue(starting_value)

        # Decorator for slider, when you move the sliderbar
        @self._value_slider.valueChanged.connect
        def _(slider_value):
            self._value_label.setText(f"{slider_value}")
            self._number_subject.updateSliderValue(slider_value)

        bottom_layout.addWidget(self._minimum_label)
        bottom_layout.addWidget(self._value_slider)
        bottom_layout.addWidget(self._maximum_label)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(bottom_layout)

        self.setLayout(layout)
