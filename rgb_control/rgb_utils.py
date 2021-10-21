from typing import List

from rgb_control.pkg_data import INTERNAL_PACKAGES

RGB_PACKAGES_PATTERNS = {
    "R": ["0703060b0000{}", "0703060c0000{}"],
    "G": ["070306090000{}", "0703060a0000{}"],
    "B": ["070306070000{}", "070306080000{}"],
}


class HexColor:
    hex_color: str

    def __init__(self, hex_color: str = "000000"):
        self.hex_color = hex_color

    @property
    def R(self) -> str:  # noqa: N802
        return self.hex_color[:2]

    @property
    def G(self) -> str:  # noqa: N802
        return self.hex_color[2:4]

    @property
    def B(self) -> str:  # noqa: N802
        return self.hex_color[4:6]

    def __getitem__(self, key: str) -> str:
        value = getattr(self, key, None)
        if value is None:
            raise KeyError
        return value


class RGBProfile:
    hex_values: HexColor
    packages: List[str]
    order_rgb_keys = ("B", "G", "R")

    def __init__(self, hex_color: HexColor):
        self.hex_color = hex_color
        self.packages_data = []
        self.__prepare_packages()

    def __create_rgb_packages(self, key: str) -> List[str]:
        rgb_packages = []
        for pattern in RGB_PACKAGES_PATTERNS[key]:
            rgb_packages.append(pattern.format(self.hex_color[key] * 58))
        return rgb_packages

    def __prepare_packages(self) -> None:
        self.packages_data = INTERNAL_PACKAGES["init"]
        for rgb_key in self.order_rgb_keys:
            self.packages_data += self.__create_rgb_packages(rgb_key)
        self.packages_data += INTERNAL_PACKAGES["final"]
