from observerPattern import Subject
from PyQt6.QtGui import QColor


# Created an own file, to prefent circular imports
class ColorHexSubject(Subject):
    _color_hex: str

    def setHexColor(self, hex_color: str) -> None:
        self._color_hex = hex_color
        self.notify()

    def getHexColor(self) -> str:
        return self._color_hex

    def setHexFromString(self, color_string: str):
        color_from_string = QColor.fromString(color_string)

        if color_from_string.isValid():
            self.setHexColor(color_from_string.name())
