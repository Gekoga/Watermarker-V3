import sys
from PyQt6.QtWidgets import (
  QWidget,
  QApplication
)

class Window(QWidget):
  def __init__(self, parent: QWidget | None) -> None:
    super().__init__(parent)
    self.setWindowTitle("Watermarker V3")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window(None)
  window.show()
  sys.exit(app.exec())
  