from typing import List, Dict

PACKAGES_DATA: Dict[str, List[str]] = {
    "init": [
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07290000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07070000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "072a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "072a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07290000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "071e0100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07090000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "072f002e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "070c0000000000000680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "070c0000000000000680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07030605000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07030601000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07030601000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07030605000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07030601000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "07030601000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    ],
    "final": [
        "07050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    ],
}

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
    def R(self) -> str:
        return self.hex_color[:2]

    @property
    def G(self) -> str:
        return self.hex_color[2:4]

    @property
    def B(self) -> str:
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

    def __return_rgb_packages(self, key: str) -> List[str]:
        rgb_packages = []
        for pattern in RGB_PACKAGES_PATTERNS[key]:
            rgb_packages.append(pattern.format(self.hex_color[key] * 58))
        return rgb_packages

    def __prepare_packages(self) -> None:
        self.packages_data = PACKAGES_DATA["init"]
        for rgb_key in self.order_rgb_keys:
            self.packages_data += self.__return_rgb_packages(rgb_key)
        self.packages_data += PACKAGES_DATA["final"]