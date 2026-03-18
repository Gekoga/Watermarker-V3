from PIL import Image, ImageFont, ImageDraw


class ImageHelper:
    TARGET_WIDTH = int(300)

    _width, _height = 0, 0
    _preview_width, _preview_height = 0, 0
    _aspect_ratio = 1
    _empty_overlay_image: Image.Image

    _font_size_preview: int

    _ink_color: list[int] = [255, 255, 255, 255]

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

        self._aspect_ratio = self._height / self._width
        self._preview_width = self.TARGET_WIDTH
        self._preview_height = int(self.TARGET_WIDTH * self._aspect_ratio)

        self._empty_overlay_image = Image.new(
            "RGBA", [self._preview_width, self._preview_height], (0, 0, 0, 0)
        )

    def getCopyOfOverlay(self) -> Image.Image | None:
        if self._width <= 0 or self._height <= 0:
            return None

        return self._empty_overlay_image.copy()

    def setFontSize(self, font_size):
        self._font_size_preview = font_size

    def setFontAlpha(self, font_alpha):
        rgb_color = self._ink_color[:3]
        self._ink_color = rgb_color

        self._ink_color.append(font_alpha)

    def setFontColor(self, font_color: list[int]):
        font_alpha = self._ink_color[-1]

        self._ink_color = font_color
        self._ink_color.append(font_alpha)

    # TODO: Be able to change the watermark, example: Diagonal over the image, multi-line or through the middle or vertical/turned 45 degrees, also found in imageContainer
    def createTextOverlay(self, overlay_text: str):
        overlay_image = self.getCopyOfOverlay()

        if overlay_image == None:
            return

        font = ImageFont.load_default(self._font_size_preview)
        overlay_draw = ImageDraw.Draw(overlay_image)

        overlay_draw.text(
            (0.0, 0.0),
            overlay_text,
            fill=tuple(self._ink_color),
            font=font,
        )

        return overlay_image
