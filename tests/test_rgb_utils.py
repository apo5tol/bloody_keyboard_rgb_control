import pytest
from rgb_control.rgb_utils import HexColor


class TestHexColor:

    color = "00ffaa"
    r = "00"
    g = "ff"
    b = "aa"

    def test_create_hex_color(self):
        hex_color = HexColor(self.color)
        assert self.color == hex_color.hex_color

    def test_hex_color_r(self):
        hex_color = HexColor(self.color)
        assert self.r == hex_color["R"]
        assert self.r == hex_color.R

    def test_hex_color_g(self):
        hex_color = HexColor(self.color)
        assert self.g == hex_color["G"]
        assert self.g == hex_color.G

    def test_hex_color_b(self):
        hex_color = HexColor(self.color)
        assert self.b == hex_color["B"]
        assert self.b == hex_color.B

    @pytest.mark.xfail(raises=KeyError, strict=True)
    def test_hex_color_wrong_key(self):
        hex_color = HexColor(self.color)
        hex_color["A"]

    @pytest.mark.xfail(raises=ValueError, strict=True)
    def test_hex_color_wrong_color(self):
        HexColor("00ffa")
