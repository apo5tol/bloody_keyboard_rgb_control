import argparse
import functools

from rgb_control.device import Keyboard
from rgb_control.rgb_utils import HexColor, RGBProfile

ID_VENDOR: int = 0x09DA
ID_PRODUCT: int = 0xFA10

all_int = functools.partial(int, base=0)


def init_argparser():
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
        type=all_int,
        help="vendor id in hex format, default: 0x09DA".format(ID_VENDOR),
        default=ID_VENDOR,
    )
    parser.add_argument(
        "-id_p",
        "--id_product",
        type=all_int,
        help="product id in hex format, default: 0xFA10".format(ID_PRODUCT),
        default=ID_PRODUCT,
    )
    return parser


def set_rgb_highlight(color, id_vendor, id_product):
    rgb_keyboard = Keyboard(id_vendor, id_product)
    rgb_color = HexColor(color)
    rgb_profile = RGBProfile(rgb_color)
    rgb_keyboard.set_rgb_highlight(rgb_profile)


def main():
    parser = init_argparser()
    args = parser.parse_args()
    set_rgb_highlight(**vars(args))


if __name__ == "__main__":
    main()
