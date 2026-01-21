from PIL import Image


class ImageHelper:
    TARGET_WIDTH = int(300)

    _width, _height = 0, 0
    _preview_width, _preview_height = 0, 0
    _empty_overlay_image: Image.Image

    def getImageFromPath(self, input_image_path: str) -> Image.Image | None:
        if input_image_path == "" or input_image_path == None:
            return None

        try:
            selected_image_file = Image.open(input_image_path)
            selected_image = selected_image_file.convert("RGBA")

            self._width, self._height = selected_image.size
            self.createOverlayForImageSize()

            return selected_image
        except IOError:
            print("File couldn't be found, or image couldn't be opened and identified ")
            return None

    def createOverlayForImageSize(self):
        if self._width <= 0 or self._height <= 0:
            return

        aspect_ratio = self._height / self._width
        self._preview_width = self.TARGET_WIDTH
        self._preview_height = int(self.TARGET_WIDTH * aspect_ratio)

        self._empty_overlay_image = Image.new(
            "RGBA", [self._preview_width, self._preview_height], (0, 0, 255, 100)
        )

    def getCopyOfOverlay(self) -> Image.Image | None:
        if self._width <= 0 or self._height <= 0:
            return None

        return self._empty_overlay_image.copy()
