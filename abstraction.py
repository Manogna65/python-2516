# without abstraction

class laptop():
    def usb_slot(self):
        pass
    def hdmi_slot(self):
        pass
    def c_port(self):
        pass

class asus(laptop):
    def usb_slot(self):
        print("asus usb slot")
    def hdmi_slot(self):
        print("asus hdmi slot")

class dell(laptop):
    def usb_slot(self):
        print("asus usb slot")
    def hdmi_slot(self):
        print("asus hdmi slot")

# user
print("buying asus laptop")
asus=asus()
asus.usb_slot()
asus.hdmi_slot()

print("buying dell laptop")
dell=dell()
dell.usb_slot()
dell.c_port()


