import math

class Circle:
    def __init__(self, radius_list):
        self.__pi = 3.141  # Private variable for pi
        self.radius_list = radius_list
class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 0  # Set your default value here
        self.inches = 0  # Set your default value here
        self.__on_off = False
        self.__volume = 50

    def increase_volume(self):
        if self.__volume < 100:
            self.__volume += 1
            print("Volume increased to", self.__volume)
        else:
            print("Volume already at maximum.")

    def decrease_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
            print("Volume decreased to", self.__volume)
        else:
            print("Volume already at minimum.")

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
            print("Channel set to", self.channel)
        else:
            print("Invalid channel. TV has only 50 channels.")

    def reset_tv(self):
        self.channel = 1
        self.__volume = 50
        print("TV reset to channel 1 and volume 50.")

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.__volume}"

class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0  # Set your default value here
        self.backlight = ''  # Set your default value here
        self.display_details = ''  # Set your default value here

    def display_details_info(self):
        # Implement the logic to display detailed features of the LED TV
        pass

class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0  # Set your default value here
        self.backlight = ''  # Set your default value here
        self.display_details = ''  # Set your default value here

    def display_details_info(self):
        # Implement the logic to display detailed features of the Plasma TV
        pass

