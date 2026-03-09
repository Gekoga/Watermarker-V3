from observerPattern import Subject
from PyQt6.QtGui import QColor


# Created an own file, to prefent circular imports
class ColorSubject(Subject):
    _color: QColor

    def setColor(self, color: QColor) -> None:
        self._color = color
        self.notify()

    def getColorString(self) -> str:
        return self._color.name()

    def getColorAsRGBList(self):
        return [self._color.red(), self._color.green(), self._color.blue()]

    def setColorFromString(self, color_string: str) -> bool:
        color_from_string = QColor.fromString(color_string)

        if color_from_string.isValid():
            self.setColor(color_from_string)
            return True

        return False
