from PIL import Image


class ImageHelper:
    _width, _height = 0, 0

    def getImageFromPath(self, input_image_path: str) -> Image.Image | None:
        if input_image_path == "" or input_image_path == None:
            return None

        try:
            selected_image_file = Image.open(input_image_path)
            return selected_image_file.convert("RGBA")
        except IOError:
            print("File couldn't be found, or image couldn't be opened and identified ")
            return None
