import argparse
import functools

from device import Keyboard
from rgb_utils import HexColor, RGBProfile

ID_VENDOR: int = 0x09DA
ID_PRODUCT: int = 0xFA10

hex_int = functools.partial(int, base=0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--color",
        type=str,
        help="color in hex format. example: 00ff00",
        required=True,
    )
    parser.add_argument(
        "-id_v",
        "--id_vendor",
        type=hex_int,
        help="vendor id in hex format, default: 0x09DA".format(ID_VENDOR),
        default=ID_VENDOR,
    )
    parser.add_argument(
        "-id_p",
        "--id_product",
        type=hex_int,
        help="product id in hex format, default: 0xFA10".format(ID_PRODUCT),
        default=ID_PRODUCT,
    )
    args = parser.parse_args()

    rgb_keyboard = Keyboard(args.id_vendor, args.id_product)
    color = HexColor(args.color)
    rgb_profile = RGBProfile(color)
    rgb_keyboard.set_rgb_highlight(rgb_profile)
