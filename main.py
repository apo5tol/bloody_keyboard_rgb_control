import json
import os

import usb.core

ID_VENDOR = 0x09DA
ID_PRODUCT = 0xFA10

PATH_TO_DEFAULT_RGB_PROFILES = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "rgb_data/default_rgb_profiles.json"
)


class Device:
    bm_request_type = 0x00000021
    b_request = 0x09
    w_value = 0x00000307
    w_index = 2

    def __init__(self, id_vendor, id_product):
        self.id_vendor = id_vendor
        self.id_product = id_product
        self.__device = None

        self.__init_device()

    def __init_device(self):
        self.__device = usb.core.find(
            idVendor=self.id_vendor, idProduct=self.id_product
        )
        if self.__device is None:
            raise ValueError("Keyboard not found!")

    def detach(self):
        for config in self.__device:
            for i in range(config.bNumInterfaces):
                if self.__device.is_kernel_driver_active(i):
                    self.__device.detach_kernel_driver(i)
        self.__device.set_configuration()

    def release(self):
        for config in self.__device:
            for i in range(config.bNumInterfaces):
                usb.util.release_interface(self.__device, i)
                self.__device.attach_kernel_driver(i)

    def set_hex_value(self, hex_value):
        self.__device.ctrl_transfer(
            self.bm_request_type,
            self.b_request,
            self.w_value,
            self.w_index,
            bytes.fromhex(hex_value),
        )


class KeyboardControl:
    def __init__(self, id_vendor, id_product):
        self.__keyboard = Device(id_vendor, id_product)

    def set_rgb_highlight(self, rgb_profile):
        self.__keyboard.detach()
        for hex_value in rgb_profile.hex_values:
            try:
                self.__keyboard.set_hex_value(hex_value)
            except usb.core.USBError:
                self.__keyboard.release()
        self.__keyboard.release()


class RGBProfile:
    def __init__(self, hex_values):
        self.hex_values = hex_values


class RGBData:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.rgb_data = {}
        self.__read_data_from_disk()

    def __read_data_from_disk(self):
        with open(self.path_to_data, "r") as rgb_data:
            self.rgb_data = json.loads(rgb_data.read())

    def get_rgb_profile(self, key):
        rgb_data = self.rgb_data.get(key)
        if rgb_data is not None:
            return RGBProfile(rgb_data)
        return None


if __name__ == "__main__":
    keyboard = KeyboardControl(ID_VENDOR, ID_PRODUCT)

    rgb_data = RGBData(PATH_TO_DEFAULT_RGB_PROFILES)

    green_rgb_profile = rgb_data.get_rgb_profile("2")
    keyboard.set_rgb_highlight(green_rgb_profile)
