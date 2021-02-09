import json
import os
from typing import Dict, List

import usb

ID_VENDOR: int = 0x09DA
ID_PRODUCT: int = 0xFA10

PATH_TO_DEFAULT_RGB_PROFILES: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "rgb_data/default_rgb_profiles.json"
)


class RGBProfile:
    hex_values: List[str]

    def __init__(self, hex_values: List[str]):
        self.hex_values = hex_values


class RGBData:
    path_to_data: str
    rgb_data: Dict[str, List[str]]

    def __init__(self, path_to_data: str):
        self.path_to_data = path_to_data
        self.rgb_data = {}
        self.__read_data_from_disk()

    def __read_data_from_disk(self) -> None:
        with open(self.path_to_data, "r") as rgb_data:
            self.rgb_data = json.loads(rgb_data.read())

    def get_rgb_profile(self, key: str) -> RGBProfile:
        rgb_data = self.rgb_data.get(key)
        if rgb_data is not None:
            return RGBProfile(rgb_data)
        return RGBProfile([])



if __name__ == "__main__":
    keyboard = KeyboardControl(ID_VENDOR, ID_PRODUCT)

    rgb_data = RGBData(PATH_TO_DEFAULT_RGB_PROFILES)

    green_rgb_profile = rgb_data.get_rgb_profile("2")
    keyboard.set_rgb_highlight(green_rgb_profile)
