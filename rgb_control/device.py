import usb

from rgb_control.rgb_utils import RGBProfile


class UsbDevice:
    bm_request_type: int = 0x00000021
    b_request: int = 0x09
    w_value: int = 0x00000307
    w_index: int = 2

    id_vendor: int
    id_product: int

    def __init__(self, id_vendor: int, id_product: int):
        self.id_vendor = id_vendor
        self.id_product = id_product
        self.__device = None

        self.__init_device()

    def __init_device(self) -> None:
        self.__device = usb.core.find(
            idVendor=self.id_vendor, idProduct=self.id_product
        )
        if self.__device is None:
            raise ValueError("Keyboard not found!")

    def detach(self) -> None:
        for config in self.__device:
            for i in range(config.bNumInterfaces):
                if self.__device.is_kernel_driver_active(i):
                    self.__device.detach_kernel_driver(i)
        self.__device.set_configuration()

    def release(self) -> None:
        for config in self.__device:
            for i in range(config.bNumInterfaces):
                usb.util.release_interface(self.__device, i)
                self.__device.attach_kernel_driver(i)

    def set_value(self, hex_value: str) -> None:
        try:
            self.__device.ctrl_transfer(
                self.bm_request_type,
                self.b_request,
                self.w_value,
                self.w_index,
                bytes.fromhex(hex_value),
            )
        except ValueError:
            self.release()
            raise


class Keyboard:
    def __init__(self, id_vendor: int, id_product: int):
        self.__keyboard_device = UsbDevice(id_vendor, id_product)

    def set_rgb_highlight(self, rgb_profile: RGBProfile) -> None:
        self.__keyboard_device.detach()
        for package_data in rgb_profile.packages_data:
            try:
                self.__keyboard_device.set_value(package_data)
            except usb.core.USBError:
                self.__keyboard_device.release()
                raise
        self.__keyboard_device.release()
