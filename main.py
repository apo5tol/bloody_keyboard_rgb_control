from device import Keyboard
from rgb_utils import HexColor, RGBProfile

ID_VENDOR: int = 0x09DA
ID_PRODUCT: int = 0xFA10


if __name__ == "__main__":
    rgb_keyboard = Keyboard(ID_VENDOR, ID_PRODUCT)
    color = HexColor("00ff00")
    rgb_profile = RGBProfile(color)
    rgb_keyboard.set_rgb_highlight(rgb_profile)
